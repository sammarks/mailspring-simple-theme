'use strict';

// Single-account Mailspring omits the native user-category collapse control.
// Add only that missing control; multi-account sections retain native behavior.
let observer;
let pending;
let emailStyles;
const states = new Map();
const prefix = 'chatgpt-theme:category-collapse:';

function enhance() {
  pending = undefined;
  document.querySelectorAll('.account-sidebar-sections > .outline-view:not(:first-child)').forEach(section => {
    const heading = section.querySelector('.heading');
    if (!heading) return;
    if (heading.querySelector('.collapse-button:not(.chatgpt-label-toggle)')) {
      const fallback = heading.querySelector('.chatgpt-label-toggle');
      if (fallback) fallback.remove();
      section.removeAttribute('data-chatgpt-collapsed');
      return;
    }
    if (heading.querySelector('.chatgpt-label-toggle')) return;
    const title = heading.querySelector('.text');
    const key = prefix + (title ? title.textContent.trim() + ':' + title.style.borderLeftColor : 'categories');
    if (!states.has(key)) {
      let collapsed = false;
      try { collapsed = localStorage.getItem(key) === 'true'; } catch (_) { /* Session-only if storage is unavailable. */ }
      states.set(key, collapsed);
    }
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'collapse-button chatgpt-label-toggle';
    const update = () => {
      const collapsed = states.get(key);
      section.setAttribute('data-chatgpt-collapsed', String(collapsed));
      button.textContent = collapsed ? 'Show' : 'Hide';
      button.setAttribute('aria-expanded', String(!collapsed));
      button.setAttribute('aria-label', `${collapsed ? 'Show' : 'Hide'} ${title ? title.textContent.trim() : 'labels'}`);
    };
    button.addEventListener('click', event => {
      event.stopPropagation();
      states.set(key, !states.get(key));
      try { localStorage.setItem(key, String(states.get(key))); } catch (_) { /* Keep the in-memory state. */ }
      update();
    });
    update();
    heading.appendChild(button);
  });
}

exports.activate = function () {
  if (observer) return;
  // index.less is the only stylesheet loaded automatically for this package.
  // Register the frame stylesheet separately so EmailFrameStylesStore finds it.
  if (typeof AppEnv !== 'undefined') {
    const sourcePath = `${__dirname}/styles/email-frame.less`;
    emailStyles = AppEnv.styles.addStyleSheet(AppEnv.themes.cssContentsOfStylesheet(sourcePath), {
      sourcePath, priority: 1,
    });
  }
  enhance();
  observer = new MutationObserver(() => {
    if (pending === undefined) pending = requestAnimationFrame(enhance);
  });
  observer.observe(document.body, { childList: true, subtree: true });
};

exports.deactivate = function () {
  if (emailStyles) emailStyles.dispose();
  emailStyles = undefined;
  if (observer) observer.disconnect();
  observer = undefined;
  if (pending !== undefined) cancelAnimationFrame(pending);
  pending = undefined;
  document.querySelectorAll('.chatgpt-label-toggle').forEach(button => button.remove());
  document.querySelectorAll('[data-chatgpt-collapsed]').forEach(section => section.removeAttribute('data-chatgpt-collapsed'));
  states.clear();
};
