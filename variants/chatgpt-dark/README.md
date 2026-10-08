# ChatGPT for Mailspring

A calm, modern theme inspired by ChatGPT's web and desktop interface: neutral
surfaces, a quiet sidebar, system typography, rounded controls, and blue accents.
Includes separately installable **ChatGPT Light** and **ChatGPT Dark** themes.

Version 1.4.8 removes the outer listbox focus outline that appears as a line
below the emails after archiving. Active-row highlighting remains visible.

Version 1.4.7 restyles action toasts as neutral floating cards with softer corners,
a subtle shadow, and clean Undo / Send now controls. The undo-send countdown
retains its timing and warning state.

Version 1.4.6 applies system typography and 16px defaults inside message frames
while preserving monospaced code, and connects RSVP choices into one button group
with Lucide check, question-mark, and X icons. The theme module registers its
email-frame stylesheet separately so Mailspring copies it into message frames.

Version 1.4.5 corrects top spacing for Mailspring’s actual nested list structure,
adding a 16px content inset above the first email.

Version 1.4.4 rounds and insets hover backgrounds, quiets the list attachment
indicator, and restyles native calendar invite cards and RSVP controls.

Version 1.4.3 hides the app's extra Unsubscribe control, makes the reply action
a compact text button, adds space above the email list, removes row dividers,
and gives search a flat neutral surface with a clear focus state.

Version 1.4.2 separates the sender disclosure caret from the name, styles the
header Unsubscribe action as a quiet rounded control, gives selected email rows
inset rounded backgrounds, and softens collapsed
messages with rounded surfaces and balanced sender, preview, and timestamp spacing.

Version 1.4.1 balances the sidebar with matching 24px insets, adds a neutral
unread pill at the edge of message rows, keeps the empty reading pane on the
content surface, and removes the composer title-bar divider.

Version 1.4 gives the main toolbar and sidebar a continuous gray surface with a
rounded content corner. Sidebar rows fit within their inset, the account switcher
clears the scrollbar, message-row stars are hidden, and label chips have balanced
spacing. Labels now has a persistent Hide/Show button even with a single account;
a small theme module adds it where Mailspring omits its native control. Formatting
pickers have more space between their icon and text. Icons use **Lucide 1.53.0**.

## Install

1. Open Mailspring.
2. Choose **Mailspring → Install New Theme…** (on Windows/Linux, look in the
   application's menu for **Install New Theme…**).
3. Select this project's root folder for **ChatGPT Light**, or select
   `variants/chatgpt-dark` for **ChatGPT Dark**.
4. Use **Change Theme…** to select the installed theme if needed.

Alternatively, extract either ZIP from `dist` and select its enclosed theme
folder. Each package is self-contained and requires no build step, downloaded
fonts, or runtime dependencies.

Installing both variants adds two choices to Mailspring's theme picker. They do
not automatically follow system appearance; select the variant you prefer.

## Preview

Open `preview/index.html` in a browser to compare the two appearances with the
**View dark theme / View light theme** button. The search field filters the
sample message list. Mail actions in this illustrative preview are decorative.

## Customize

Edit `styles/ui-variables.less` for the light palette. The dark variant's palette
is in `variants/chatgpt-dark/styles/ui-variables.less`; its final declarations
override the light defaults. Adjust `@accent-primary` for links and focus rings,
and `@btn-emphasis-bg-color` for primary buttons. Keep button labels readable
against any replacement color.

`styles/components.less` contains the component overrides; the dark package has
its own copy so it can be installed independently. Make shared component edits
in both copies. `styles/refinements.less` contains composer, label, account-dot,
and typography adjustments. `styles/icons.less` embeds Lucide SVG
masks for the app’s UI assets; neither file changes Mailspring application code. After installation, Mailspring copies the theme into its packages
directory, so edits in this project need to be reinstalled. On macOS, the installed
copy is under `~/Library/Application Support/Mailspring/packages/`.

The theme preserves virtualized message-row dimensions, window drag regions,
and email content. It styles email containers rather than globally recoloring
HTML email images or branded content. Mailspring controls HTML email rendering
inside its separate frame, so individual email designs may retain their own colors.

## Validation

Verified with the styles and Less **3.13.1** version from installed Mailspring
**1.26.0**. Both variants compile successfully with the core stylesheet,
email-frame, thread-list, message-list, and composer styles. The browser previews
were rendered and visually inspected in Chromium. A browser fixture using
Mailspring’s core and component styles also verifies the macOS toolbar group
shadows, button borders, neutral selection colors, and unboxed message container.
Composer checks cover split and single-action Send buttons, removal of gradients
and formatting dividers, account-color preservation, label inline overrides,
sidebar indentation, and SVG icon masks. Version 1.4 additionally checks actual ScrollRegion sizing, scrollbar hit testing,
single-account collapse persistence and cleanup, and exact
heading/selection alignment, visible collapse controls, hidden unused disclosure
slots, preservation of nested-folder arrows, and sender/subject weight differences. Live mailbox appearance has
not been verified inside Mailspring.

## References

- [Official Mailspring theme starter](https://github.com/Foundry376/Mailspring-Theme-Starter)
- [Mailspring source and base styles](https://github.com/Foundry376/Mailspring)
- [ChatGPT appearance and accent options](https://help.openai.com/en/articles/11958281-updating-your-visual-experience-on-chatgpt)

Independent, unofficial theme; not affiliated with OpenAI or Mailspring.

## License

Theme code: MIT; see `LICENSE.md`. Lucide icons: ISC; see
`vendor/lucide/LICENSE`. The SVG sources, pinned version, and asset mappings are
in `vendor/lucide`; regenerate with `python3 scripts/generate-lucide-icons.py`.
This uses the vendored sources and requires no npm installation. App/provider
logos, emoji artwork, and email content keep their original rendering.
