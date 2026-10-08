"""Generate theme SVG masks from the vendored Lucide 1.53.0 icons."""
from pathlib import Path
from urllib.parse import quote
import json, re, os
ROOT = Path(__file__).resolve().parents[1]
VENDOR = ROOT / 'vendor/lucide/icons'
SVG_SOURCE = Path(os.environ.get('LUCIDE_SOURCE', str(VENDOR)))

# Named application artwork and provider logos are not action icons.
ART = ('/composer-emoji/', '/providers/', 'mailspring.png', 'transparency-background',
       'tooltip-bg-', 'sidebar-section-divider', 'onboarding-divider', 'slider-',
       'facebook-icon', 'linkedin-icon', 'twitter-icon', 'nylas-identity-',
       'volstead-', 'icons-bg', 'pro-plugins', 'activity-loading-mask',
       )
EXACT = {
'icon-attachment-download':'download','top-signature-dropdown':'signature',
'inbox-zero-plain':'inbox','activity-list-empty':'activity',
'inbox':'inbox','unread':'mail-open','archive':'archive','drafts':'file-pen-line',
'folder':'folder','important':'bookmark','junk':'shield-alert','spam':'shield-alert',
'label':'tag','tag':'tag','people':'users','person':'user-round','plugins':'puzzle',
'reminders':'bell','sent':'send','snoozed':'clock','starred':'star','today':'calendar-days',
'trash':'trash-2','activity':'activity','icon':'activity','Today_Sun':'sun',
'close-linux':'x','maximize-linux':'square','minimize-linux':'minus','windows-menu-icon':'menu',
'attachment-quicklook':'scan-eye','file-doc':'file-text','file-docx':'file-text',
'file-fallback':'file','file-ics':'calendar','file-pdf':'file-text','file-ppt':'presentation',
'file-pptx':'presentation','file-xls':'sheet','file-xlsx':'sheet','file-zip':'file-archive',
'ic-attachments-all-clippy':'paperclip','ic-attachments-download-all':'download',
'image-cancel-button':'x','image-download-button':'download','remove-attachment':'x',
'composer-caret':'chevron-down','composer-drop-to-attach':'paperclip','composer-popout':'square-arrow-out-up-right',
'icon-composer-attachment':'paperclip','icon-composer-dropdown':'chevron-down',
'icon-composer-emoji':'smile','icon-composer-eye':'eye','icon-composer-linktracking':'link',
'icon-composer-mailmerge':'mail-plus','icon-composer-overflow':'ellipsis',
'icon-composer-reminders':'circle-check','icon-composer-send':'arrow-up',
'icon-composer-sendlater':'clock','icon-composer-trash':'trash-2',
'icon-composer-grammar':'spell-check','icon-composer-templates':'file-text',
'icon-composer-translate':'languages','icon-tracking-opened':'eye',
'ic-tracking-unvisited':'link','ic-tracking-visited':'link-2',
'icon-sidebar-addcategory':'plus','icon-alert-onred':'triangle-alert',
'icon-alert-sourcelist':'triangle-alert','icon-accounts-addnew':'user-round-plus',
'ic-contact-profile-modal':'contact-round','ic-send-later-modal':'clock',
'ic-send-reminders-modal':'bell','ic-snooze-modal':'clock','ic-translation-modal':'languages',
'activity-drill-down-arrow':'chevron-right','icon-activity-linkopen':'link',
'icon-activity-mailopen':'mail-open','icon-activity-replied':'reply','icon-toolbar-activity':'activity',
'ic-calendar-left-arrow':'chevron-left','ic-calendar-month':'calendar-days','ic-calendar-right-arrow':'chevron-right',
'dropdown-chevron':'chevron-down','edit-icon':'pencil',
'ic-eventcard-calendar':'calendar','ic-eventcard-description':'file-text',
'ic-eventcard-disclosure':'chevron-down','ic-eventcard-link':'link',
'ic-eventcard-location':'map-pin','ic-eventcard-notes':'sticky-note',
'ic-eventcard-people':'users','ic-eventcard-reminder':'bell','ic-eventcard-time':'clock',
'icon-RSVP-calendar-mini':'calendar-check','chevron-double-native':'chevrons-up-down',
'chevron-dropdown-native':'chevron-down','icon-align-center':'align-center',
'icon-align-left':'align-left','icon-align-right':'align-right','icon-bold':'bold',
'icon-bold-active':'bold','icon-indent':'indent-increase','icon-italic':'italic',
'icon-italic-active':'italic','icon-list':'list','icon-quote':'quote',
'icon-underline':'underline','icon-underline-active':'underline',
'label-x':'x','tagging-checkbox':'square','tagging-checkmark':'check','tagging-conflicted':'minus',
'btn-column-minus':'minus','btn-column-plus':'plus','icon-column-minus':'minus',
'icon-column-plus':'plus','mailmerge-grabber':'grip-vertical',
'checked':'check','checked-selected':'check','collapse':'chevron-up','expand':'chevron-down',
'ic-findinthread-close':'x','ic-findinthread-next':'chevron-down','ic-findinthread-previous':'chevron-up',
'icon-attachment-':'paperclip','message-actions-ellipsis':'ellipsis',
'message-disclosure-triangle':'chevron-down','message-disclosure-triangle-active':'chevron-down',
'print':'printer','reply-all-footer':'reply-all','reply-footer':'reply',
'thread-popin':'minimize-2','thread-popout':'square-arrow-out-up-right',
'toolbar-down-arrow':'chevron-down','toolbar-up-arrow':'chevron-up',
'icon-thread-hidesidebar':'panel-right-close','icon-thread-showsidebar':'panel-right-open',
'modal-close':'x','icon-copytoclipboard':'copy','onboarding-back':'arrow-left','onboarding-close':'x',
'appearance-mode-list':'list','appearance-mode-split':'columns-2','appearance-mode-splitVertical':'rows-2',
'appearance-scale-big':'a-large-small','appearance-scale-small':'a-large-small',
'ic-refresh':'refresh-cw','ic-upgrade':'circle-arrow-up','pro-feature-checkmark':'check',
'pro-feature-ring':'circle-check','pro-feature-translation':'languages','rules-big':'list-filter',
'plugin-icon-default':'puzzle','theme-icon-default':'palette','signatures-big':'signature',
'ic-dropdown-forward':'forward','ic-dropdown-reply':'reply','ic-dropdown-replyall':'reply-all',
'ic-dropdown-whitespace':'remove-formatting','ic-message-button-reply':'reply',
'searchclear':'x','searchloupe':'search','sheet-back':'arrow-left','account-switcher-dropdown':'chevron-down',
'icon-phone':'phone','checkbox-checkmark':'check','checkbox-checkmark-activerow':'check',
'ic-timestamp-reminder':'bell','ic-timestamp-snooze':'clock','icon-draft-pencil':'pencil',
'icon-forwarded-':'forward','icon-reminder-outline':'bell','icon-reminder':'bell-ring',
'icon-replied-':'reply','icon-snoozed':'clock','icon-star-':'star','icon-star-action-hover-':'star',
'icon-star-hover-':'star','icon-thread-disclosure':'chevron-down','icon-thread-reply':'reply',
'icon-unread-':'circle','in-label-bell':'bell','undo-icon':'undo-2',
'ic-quick-button-archive':'archive','ic-quick-button-trash':'trash-2','ic-quickaction-snooze':'clock',
'ic-toolbar-native-reminder':'bell','ic-toolbar-native-share':'share-2','tiny-warning-sign':'triangle-alert',
'icon-preferences-accounts':'users','icon-preferences-appearance':'palette',
'icon-preferences-encryption':'lock-keyhole','icon-preferences-folders':'folder',
'icon-preferences-general':'settings','icon-preferences-mail-rules':'list-filter',
'icon-preferences-mcp':'plug','icon-preferences-plugins':'puzzle',
'icon-preferences-shortcuts':'keyboard','icon-preferences-signatures':'signature',
'icon-preferences-subscription':'credit-card','icon-preferences-templates':'file-text',
}
TOOLBAR = {'archive':'archive','attach':'paperclip','bulb-off':'lightbulb','bulb-on':'lightbulb',
'chevron':'chevron-down','compose':'square-pen','dropdown-chevron':'chevron-down',
'export-contact':'contact-round','folder':'folder','forward':'forward','icon-toggle-pane':'panel-right',
'markasread':'mail-open','markasunread':'mail','more':'ellipsis','movetofolder':'folder-input',
'not-spam':'shield-check','person-sidebar':'user-round','popout':'square-arrow-out-up-right',
'reply-all':'reply-all','reply':'reply','send':'send','snooze':'clock','spam':'shield-alert',
'star-selected':'star','star':'star','style':'type','tag':'tag','templates':'file-text','trash':'trash-2'}
FA = {'bold':'bold','italic':'italic','underline':'underline','strikethrough':'strikethrough',
'link':'link','list':'list','list-ol':'list-ordered','list-ul':'list','quote-left':'quote',
'smile-o':'smile','sticky-note-o':'sticky-note','tag':'tag','text-height':'a-large-small',
'star':'star','star-o':'star'}

def lookup(path, name):
    if name in EXACT: return EXACT[name]
    if name.startswith('ic-emptystate-'):
        return {'archive':'archive','drafts':'file-pen-line','important':'bookmark','n1-snoozed':'clock','reminders':'bell','sent':'send','spam':'shield-alert','starred':'star','trash':'trash-2'}[name.removeprefix('ic-emptystate-')]
    if name.startswith('toolbar-'): return TOOLBAR.get(name[8:])
    if name.startswith('tooltip-'): return name.split('-')[1]
    if name.startswith('Icon-Important-'): return 'bookmark'
    if name.startswith('icon-swipe-'): return {'archive':'archive','snooze':'clock','trash':'trash-2'}[name[11:]]
    if name.startswith('ic-snoozepopover-'):
        return {'later':'clock','month':'calendar-days','tomorrow':'sunrise','tonight':'moon','week':'calendar-days','weekend':'calendar-days'}[name.removeprefix("ic-snoozepopover-")]
    if name == 'ic-modal-image':
        return {'composer-grammar-check':'spell-check','link-tracking':'link','open-tracking':'eye',
                'thread-sharing':'share-2','thread-unsubscribe':'mail-minus'}[path.split('/')[2]]
    return None

def uri(name, color='black'):
    source = VENDOR / (name + '.svg')
    if not source.exists():
        source.parent.mkdir(parents=True, exist_ok=True)
        source.write_bytes((SVG_SOURCE / (name + '.svg')).read_bytes())
    svg = re.sub(r'<!--.*?-->', '', source.read_text(), flags=re.S).replace('currentColor', color)
    return 'data:image/svg+xml,' + quote(re.sub(r'\s+', ' ', svg).strip(), safe='')

def mask(name):
    return f'-webkit-mask-image: url("{uri(name)}") !important; mask-image: url("{uri(name)}") !important;'

assets = json.loads((ROOT/'scripts/mailspring-ui-assets.json').read_text())
css = ['// Generated from vendored Lucide 1.53.0 (ISC). See vendor/lucide/LICENSE.']
manifest, excluded, unknown = {}, [], []
for path in assets:
    if any(part in path for part in ART): excluded.append(path); continue
    name = re.sub(r'@\dx', '', Path(path).stem)
    icon = lookup(path, name)
    if icon is None: unknown.append(path); continue
    manifest[path] = icon
    if '/internal_packages' in path:
        fragment = '/'.join(path.split('/')[2:-1]) + '/' + name
    else: fragment = '/'.join(path.split('/')[-2:-1]) + '/' + name
    # @ distinguishes retina variants from another icon with a longer name.
    fragment += '@' if '@' in path else '.'
    selector = f'body img[src*="{fragment}"]'
    css.append(f'''{selector} {{
  content: url("{uri(icon)}");
  width: 18px !important; height: 18px !important; zoom: 1 !important;
  filter: @chatgpt-icon-filter;
}}
{selector}.content-mask {{
  content: normal;
  {mask(icon)}
  -webkit-mask-size: 100% 100% !important; mask-size: 100% 100% !important;
  -webkit-mask-repeat: no-repeat; mask-repeat: no-repeat;
  -webkit-mask-position: center; mask-position: center;
  filter: none !important;
}}''')
if unknown: raise SystemExit('Unmapped UI assets:\n'+'\n'.join(unknown))
css.append('body img[src*="/empty-state/"], body img[src*="inbox-zero-plain"] { width: 72px !important; height: 72px !important; }\nbody img[src*="/attachments/file-"] { width: 32px !important; height: 32px !important; }')
for old, icon in FA.items():
    css.append(f'''body .fa-{old} {{
  display: inline-block; width: 18px; height: 18px; vertical-align: middle;
  font-size: 0;
}}
body .fa-{old}:before {{
  content: ''; display: block; width: 100%; height: 100%;
  background: currentColor; {mask(icon)}
  -webkit-mask-size: contain; mask-size: contain;
  -webkit-mask-repeat: no-repeat; mask-repeat: no-repeat;
}}''')
# CSS-drawn and background-image icons do not use RetinaImg.
backgrounds = {
'.thread-list .thread-icon.thread-icon-attachment':'paperclip',
'.thread-list .thread-icon.thread-icon-replied':'reply',
'.thread-list .thread-icon.thread-icon-forwarded':'forward',
'.thread-list .thread-icon.thread-icon-star':'star',
'.thread-list .thread-icon.thread-icon-star-on-hover':'star',
'.thread-list .thread-icon.thread-icon-unread':'circle',
'.thread-list .list-item:hover .thread-icon.thread-icon-none':'star',
'.thread-list .thread-icon.thread-icon-star:hover':'star',
'.thread-list .thread-icon.thread-icon-star-on-hover:hover':'star',
'.thread-list .list-item .list-column-HoverActions .action.action-archive':'archive',
'.thread-list .list-item .list-column-HoverActions .action.action-trash':'trash-2',
'.thread-list .list-item .list-column-HoverActions .action.action-snooze':'clock',
'.thread-list .list-item.selected .list-column-HoverActions .action.action-archive':'archive',
'.thread-list .list-item.selected .list-column-HoverActions .action.action-trash':'trash-2',
'.thread-list .list-item.selected .list-column-HoverActions .action.action-snooze':'clock',
'.thread-list .list-item.focused .list-column-HoverActions .action.action-archive':'archive',
'.thread-list .list-item.focused .list-column-HoverActions .action.action-trash':'trash-2',
'.thread-list .list-item.focused .list-column-HoverActions .action.action-snooze':'clock',
'#message-list .collapsed-attachment':'paperclip',
'.menu .item .checkmark':'check',
'.list-tabular .list-tabular-item.selected .checkmark .inner':'check',
'.list-tabular .list-tabular-item.selected.focused .checkmark .inner':'check',
'.window-controls .close':'x', '.window-controls .minimize':'minus', '.window-controls .maximize':'square',
}
for selector, icon in backgrounds.items():
    color = 'white' if 'selected .checkmark' in selector else 'black'
    css.append(f'body {selector} {{ background-image: url("{uri(icon,color)}"); background-size: 18px 18px; background-repeat: no-repeat; background-position: center; }}')
css.append(f'''body .disclosure-triangle div {{
  border: 0; width: 12px; height: 12px; background: @text-color-subtle;
  {mask('chevron-right')} -webkit-mask-size: contain; mask-size: contain;
}}
body .RichEditor-toolbar .color-picker > button {{
  position: relative; min-width: 32px; min-height: 32px;
  border-radius: 7px; overflow: hidden; padding: 0;
}}
body .RichEditor-toolbar .color-picker > button:before {{
  content: ''; position: absolute; inset: 0 0 3px; background: @background-primary;
}}
body .RichEditor-toolbar .color-picker > button:after {{
  content: ''; position: absolute; width: 18px; height: 18px; left: calc(50% - 9px); top: calc(50% - 9px);
  background: @text-color; {mask('baseline')} -webkit-mask-size: contain; mask-size: contain;
}}
body .RichEditor-toolbar select {{
  -webkit-appearance: none; appearance: none; padding-right: 18px;
  background-image: url("{uri('chevron-down')}");
  background-repeat: no-repeat; background-position: right center; background-size: 12px 12px;
}}''')
(ROOT/'styles/icons.less').write_text('\n\n'.join(css)+'\n')
(ROOT/'vendor/lucide/mapping.json').write_text(json.dumps({'version':'1.53.0','imageAssets':manifest,'fontIcons':FA,'backgroundIcons':backgrounds,'artworkAndBranding':excluded},indent=2)+'\n')
print(f'Generated {len(manifest)} image mappings, {len(FA)} font icons, {len(backgrounds)} background icons; {len(excluded)} non-action artwork assets retained.')
