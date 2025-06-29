[Skip to main content](https://firebase.google.com/docs/studio/set-up-gemini#main-content)

[![Firebase](https://www.gstatic.com/devrel-devsite/prod/v18c0c2eee8563a4b6cc1af57fb933ddf1b6767fab13f530923a6c204c8d00f83/firebase/images/lockup.svg)](https://firebase.google.com/)

`/`

- [English](https://firebase.google.com/docs/studio/set-up-gemini)
- [Deutsch](https://firebase.google.com/docs/studio/set-up-gemini?hl=de)
- [Español – América Latina](https://firebase.google.com/docs/studio/set-up-gemini?hl=es-419)
- [Français](https://firebase.google.com/docs/studio/set-up-gemini?hl=fr)
- [Indonesia](https://firebase.google.com/docs/studio/set-up-gemini?hl=id)
- [Italiano](https://firebase.google.com/docs/studio/set-up-gemini?hl=it)
- [Polski](https://firebase.google.com/docs/studio/set-up-gemini?hl=pl)
- [Português – Brasil](https://firebase.google.com/docs/studio/set-up-gemini?hl=pt-br)
- [Tiếng Việt](https://firebase.google.com/docs/studio/set-up-gemini?hl=vi)
- [Türkçe](https://firebase.google.com/docs/studio/set-up-gemini?hl=tr)
- [Русский](https://firebase.google.com/docs/studio/set-up-gemini?hl=ru)
- [עברית](https://firebase.google.com/docs/studio/set-up-gemini?hl=he)
- [العربيّة](https://firebase.google.com/docs/studio/set-up-gemini?hl=ar)
- [فارسی](https://firebase.google.com/docs/studio/set-up-gemini?hl=fa)
- [हिंदी](https://firebase.google.com/docs/studio/set-up-gemini?hl=hi)
- [বাংলা](https://firebase.google.com/docs/studio/set-up-gemini?hl=bn)
- [ภาษาไทย](https://firebase.google.com/docs/studio/set-up-gemini?hl=th)
- [中文 – 简体](https://firebase.google.com/docs/studio/set-up-gemini?hl=zh-cn)
- [中文 – 繁體](https://firebase.google.com/docs/studio/set-up-gemini?hl=zh-tw)
- [日本語](https://firebase.google.com/docs/studio/set-up-gemini?hl=ja)
- [한국어](https://firebase.google.com/docs/studio/set-up-gemini?hl=ko)

[Blog](https://firebase.blog/) [Studio](https://studio.firebase.google.com/) [Go to console](https://console.firebase.google.com/)

[Sign in](https://firebase.google.com/_d/signin?continue=https%3A%2F%2Ffirebase.google.com%2Fdocs%2Fstudio%2Fset-up-gemini&prompt=select_account)

- [Documentation](https://firebase.google.com/docs)
- [Firebase Studio](https://firebase.google.com/docs/studio)

- On this page
- [Use Gemini in Firebase in your workspace](https://firebase.google.com/docs/studio/set-up-gemini#add-ai)
  - [Gemini in Firebase shortcuts](https://firebase.google.com/docs/studio/set-up-gemini#shortcuts)
- [Adjust your code completion settings](https://firebase.google.com/docs/studio/set-up-gemini#adjust-code-complete)
- [Adjust your codebase indexing settings](https://firebase.google.com/docs/studio/set-up-gemini#adjust-code-indexing)
- [Customize instructions for Gemini in Firebase with an AI rules file](https://firebase.google.com/docs/studio/set-up-gemini#custom-instructions)
  - [Create and test your AI rules file](https://firebase.google.com/docs/studio/set-up-gemini#create-ai-rules)
  - [Example](https://firebase.google.com/docs/studio/set-up-gemini#example)
- [Exclude files from Gemini with .aiexclude files](https://firebase.google.com/docs/studio/set-up-gemini#exclude-files)
  - [How to write .aiexclude files](https://firebase.google.com/docs/studio/set-up-gemini#write-aiexclude-files)
  - [Examples](https://firebase.google.com/docs/studio/set-up-gemini#examples)
- [Bring your own key: Use other Gemini models in chat](https://firebase.google.com/docs/studio/set-up-gemini#byok)
- [Next steps](https://firebase.google.com/docs/studio/set-up-gemini#next-steps)

Here's everything we announced at I/O, from new Firebase Studio features to more ways to integrate AI. [Read blog.](https://firebase.blog/posts/2025/05/whats-new-at-google-io)

- [Firebase](https://firebase.google.com/)
- [Documentation](https://firebase.google.com/docs)
- [Firebase Studio](https://firebase.google.com/docs/studio)
- [AI](https://firebase.google.com/docs/ai)

Was this helpful?



 Send feedback



# Configure Gemini in Firebase within workspaces  bookmark\_border   Stay organized with collections     Save and categorize content based on your preferences.

- On this page
- [Use Gemini in Firebase in your workspace](https://firebase.google.com/docs/studio/set-up-gemini#add-ai)
  - [Gemini in Firebase shortcuts](https://firebase.google.com/docs/studio/set-up-gemini#shortcuts)
- [Adjust your code completion settings](https://firebase.google.com/docs/studio/set-up-gemini#adjust-code-complete)
- [Adjust your codebase indexing settings](https://firebase.google.com/docs/studio/set-up-gemini#adjust-code-indexing)
- [Customize instructions for Gemini in Firebase with an AI rules file](https://firebase.google.com/docs/studio/set-up-gemini#custom-instructions)
  - [Create and test your AI rules file](https://firebase.google.com/docs/studio/set-up-gemini#create-ai-rules)
  - [Example](https://firebase.google.com/docs/studio/set-up-gemini#example)
- [Exclude files from Gemini with .aiexclude files](https://firebase.google.com/docs/studio/set-up-gemini#exclude-files)
  - [How to write .aiexclude files](https://firebase.google.com/docs/studio/set-up-gemini#write-aiexclude-files)
  - [Examples](https://firebase.google.com/docs/studio/set-up-gemini#examples)
- [Bring your own key: Use other Gemini models in chat](https://firebase.google.com/docs/studio/set-up-gemini#byok)
- [Next steps](https://firebase.google.com/docs/studio/set-up-gemini#next-steps)

Firebase Studio facilitates your development workflows with the following
AI-assisted code features:

- Suggested code completion as you type.

- AI assistance with chat, which is
workspace-aware and fully-integrated with your code. It can generate,
translate, and explain code. And, with your review and approval,
Gemini in Firebase can directly interact with your workspace to
update files, run terminal commands, interpret command output, and
determine next steps. Learn more at [Try\\
chat with Gemini](https://firebase.google.com/docs/studio/try-gemini#ai-chat).

- Inline actions that you can take on selected pieces of code. For
example, you can ask Gemini to make the selected
code more readable.

- Inline code assistance.


You can customize how Gemini in Firebase helps you by adjusting its
settings and adding AI rules files:

- [Adjust code completion settings](https://firebase.google.com/docs/studio/set-up-gemini#adjust-code-complete).
- [Adjust your codebase indexing settings](https://firebase.google.com/docs/studio/set-up-gemini#adjust-code-indexing).
- [Customize instructions for Gemini with an AI rules\\
file](https://firebase.google.com/docs/studio/set-up-gemini#custom-instructions).
- [Exclude files from Gemini with `.aiexclude`\\
files](https://firebase.google.com/docs/studio/set-up-gemini#exclude-files).
- [Bring your own key: Use other Gemini models in chat](https://firebase.google.com/docs/studio/set-up-gemini#byok)

## Use Gemini in Firebase in your workspace

Use Gemini in Firebase to boost your coding productivity through the
[chat panel](https://firebase.google.com/docs/studio/try-gemini#chat) or
[inline code](https://firebase.google.com/docs/studio/try-gemini#inline-chat) assistance.

1. Use either chat or inline code assistance in your
workspace:

   - To use chat: In your open workspace, click
     spark **Gemini** at
     the bottom of the workspace.

   - To use inline code assistance: Start typing your code and press `Tab` to
     accept suggestions.
2. Be aware that the following two options are enabled by default:


   - **Suggestions as you type**, which provides inline code completion.
   - **Codebase indexing**, which provides better customization and more
     helpful responses.

To change these selections for your workspace settings in the
future:

   - To update code completion settings, see
     [Adjust your code completion settings](https://firebase.google.com/docs/studio/set-up-gemini#adjust-code-complete).
   - To update code indexing settings, see
     [Adjust your code indexing settings](https://firebase.google.com/docs/studio/set-up-gemini#adjust-code-indexing).

You can also exclude specific files and directories from AI indexing. See
[Exclude files from Gemini with `.aiexclude` files](https://firebase.google.com/docs/studio/set-up-gemini#exclude-files).

### Gemini in Firebase shortcuts

To quickly open chat with Gemini: press
`Ctrl+Shift+Space` (or `Cmd+Shift+Space` on MacOS).

To view Gemini commands from the command palette:

1. Open the command palette by pressing `Ctrl+Shift+P` (or `Cmd+Shift+P` on
MacOS).

2. Search for **Gemini**.

A list of Gemini commands appears.


## Adjust your code completion settings

To help you write code, Firebase Studio provides AI code
completion that predicts and autofills code in any open file as soon as you
begin to type.

Be aware that _**code completion is turned on by default**_.

To toggle code completion on or off, adjust your code completion settings using
one of the following methods:

- If you use a `settings.json` file, set
`"IDX.aI.enableInlineCompletion"` to `true` or `false`.

- To update settings in the Firebase Studio workspace:

1. Click ![Gear icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-gear.svg)**Manage** (located at the bottom left of the workspace), then choose
     Settings, or press `Ctrl+,` ( `Cmd+,` on Mac).

     If you're using the App Prototyping agent in
     Prototyper
     view, click ![Code switch icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-code.svg)**Switch to Code** to open Code view.

2. Select the **Workspace** tab, then search for the
     **Firebase Studio \> AI > Enable Inline**
     **Completion** setting.

3. To turn off code completion, deselect the
     **Enable inline code completion as you type** option.

## Adjust your codebase indexing settings

You can control whether Gemini indexes your code.
Indexing your code provides more helpful results when using chat or inline
AI assistance.

Be aware that _**codebase indexing is turned on by default**_.

To toggle code indexing on or off, adjust your codebase indexing settings using
one of the following methods:

- If you use a `settings.json` file, set
`"IDX.aI.enableCodebaseIndexing"`
to `true` or `false`.

- To update settings in the Firebase Studio workspace:

1. Click ![Gear icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-gear.svg)**Manage** (located at the bottom left of the workspace), then choose
     Settings, or pres `Ctrl+,` ( `Cmd+,` on Mac).

     If you're using the App Prototyping agent in
     Prototyper
     view, click ![Code switch icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-code.svg)**Switch to Code** to open Code view.

2. Select the **Workspace** tab, then search for the
     **Firebase Studio \> AI > Enable Inline Completion** setting.

3. Select **Firebase Studio** \> **AI: Enable Codebase**
     **Indexing**.

4. To turn off code indexing, deselect **AI: Enable Codebase Indexing**.
     You must update code indexing settings for each of your workspaces.

## Customize instructions for Gemini in Firebase with an AI rules file

You can add context and system prompt information by creating an AI rules
file ( `.idx/airules.md`). Gemini in Firebase uses your rules as system
instructions and context, ensuring that its responses are customized for your
use case.

Use the AI rules file to share custom prompts, best practices, and even
important context about your project with Gemini to achieve
goals like:

- Influencing Gemini's persona and specializing its expertise.
- Applying project-wide standards, like coding style, conventions, and
technology preferences.
- Reducing the amount of information you need to share explicitly in code or
chat by providing essential context about your project.

The rules you configure are used by Gemini in
[chat](https://firebase.google.com/docs/studio/try-gemini#chat).

### Create and test your AI rules file

To create and test your AI rules file:

1. Create a new file at `.idx/airules.md` in your Firebase Studio
workspace (in the same directory as your
[`dev.nix`](https://firebase.google.com/docs/studio/customize-workspace) file). You can use one of
the following options:

   - From **Explorer** ( `Ctrl+Shift+E`), right-click on **.idx** and select
     **New file**. Name the file `airules.md` and press Enter.
   - From the terminal, use your preferred text editor to open
     `.idx/airules.md`.
2. Add content to the file. You may want to add information about the persona
Gemini should use (like "You are an expert developer and
helpful assistant who knows everything about Next.js"), coding and
conversation standards, and context about the project. See the
following [Example](https://firebase.google.com/docs/studio/set-up-gemini#example) for
an example AI rules file.

3. Save the file and [open\\
Gemini in Firebase](https://firebase.google.com/docs/studio/try-gemini#chat).

4. To start using your AI rules, you can do one of the following:

   - Rebuild the workspace by refreshing the page. After you rebuild,
     Gemini in Firebase will use the rules file within chat.
     Changes to the AI
     rules file should be reflected in chat immediately.
   - If you don't want to rebuild your workspace, you can ask
     Gemini using chat to
     `load airules.md`. If you make changes to
     the file during the current session, you may need to re-prompt
     Gemini to load the rules file again.
5. Ask questions about your code. Gemini responds using
the information you included in the rules file as context.


### Example

The following is a basic example of a rules file that you might use for a
casual game developed with Next.js:

```
# Persona

You are an expert developer proficient in both front- and back-end development
with a deep understanding of Node.js, Next.js, React, and Tailwind CSS. You
create clear, concise, documented, and readable TypeScript code.

You are very experienced with Google Cloud and Firebase services and how
you might integrate them effectively.

# Coding-specific guidelines

- Prefer TypeScript and its conventions.
- Ensure code is accessible (for example, alt tags in HTML).
- You are an excellent troubleshooter. When analyzing errors, consider them
  thoroughly and in context of the code they affect.
- Do not add boilerplate or placeholder code. If valid code requires more
  information from the user, ask for it before proceeding.
- After adding dependencies, run `npm i` to install them.
- Enforce browser compatibility. Do not use frameworks/code that are not
  supported by the following browsers: Chrome, Safari, Firefox.
- When creating user documentation (README files, user guides), adhere to the
  Google developer documentation style guide
  (https://developers.google.com/style).

# Overall guidelines

- Assume that the user is a junior developer.
- Always think through problems step-by-step.

# Project context

- This product is a web-based strategy game with a marine life theme.
- Intended audience: casual game players between the ages of 17 and 100.

```

## Exclude files from Gemini with `.aiexclude` files

You can control which files in your codebase should be kept hidden from
Gemini by including `.aiexclude` files in your project.
This lets you granularly control the project context you share with
Gemini.

Much like a `.gitignore` file, an `.aiexclude` file tracks files that
shouldn't be shared with Gemini, including the chat
experience as well as AI features that operate in the editor. An `.aiexclude`
file operates on files at or below the directory that contains it.

Files covered by `.aiexclude` won't be indexed by Gemini when
**Codebase Indexing** is enabled. Additionally, `.aiexclude` will affect inline
assistance for covered files in the following ways:

- **Chat assistance**: Gemini won't be able to answer
questions or offer suggestions about files covered by `.aiexclude`.
- **Code completion**: Suggested code completions will not be available when
editing covered files.
- **Inline assistance**: You'll be able to generate new code, but not modify
existing code when editing covered files.

Other development environments such as [Android\\
Studio](https://developer.android.com/studio/preview/gemini/aiexclude) may also
honor `.aiexclude` files.

### How to write `.aiexclude` files

An `.aiexclude` file follows the same syntax as a `.gitignore` file, with these
following differences:

- An empty `.aiexclude` file blocks all files in its directory and all
sub-directories. This is the same as a file that contains `**/*`.
- `.aiexclude` files don't support negation (prefixing patterns with `!`).

### Examples

Here are some example `.aiexclude` file configurations:

- Block all files named `apikeys.txt` at or below the directory that contains
the `.aiexclude` file:








```
apikeys.txt

```

- Block all files with the `.key` file extension at or below the directory that
contains the `.aiexclude` file:








```
*.key

```

- Block only the `apikeys.txt` file at the in the same directory as the
`.aiexclude`, but not any subdirectories:








```
/apikeys.txt

```

- Block all files in the directory `my/sensitive/dir` and all subdirectories.
The path should be relative to the directory that contains the `.aiexclude`
file:








```
my/sensitive/dir/

```


## Bring your own key: Use other Gemini models in chat

You can configure the Gemini model that [Gemini in Firebase\\
chat](https://firebase.google.com/docs/studio/try-gemini) uses. You have a choice of the built-in model,
models configured in the chat window (including
Gemini 2.5 models), or any Gemini model to which you have
access.

For a list of all available models, see [Gemini\\
models](https://ai.google.dev/gemini-api/docs/models).

**To configure your key and select a different Gemini model:**

1. In your open workspace, click
spark **Gemini** at
the bottom of the workspace (or the **Gemini** tab).

2. In the Gemini in Firebase chat window, click the model name
drop-down, then click the **Gemini API key** link. **User Settings**
appear.

3. In the **IDX > AI: Gemini Api Key** field,
enter your Gemini API key.


You can now select any of the pre-configured Gemini models in
chat.

**To configure a Gemini model that isn't in the drop-down:**

1. Identify the Gemini model you want to use in
chat from the list at
[Gemini models](https://ai.google.dev/gemini-api/docs/models).
For example, you'd enter `gemini-2.0-flash-lite` to
use the latest stable
[Gemini 2.0 Flash‑Lite model](https://ai.google.dev/gemini-api/docs/models#gemini-2.0-flash-lite).

2. From the Gemini in Firebase chat window,
click the model selector, then choose **Custom model ID**. **User**
**Settings** opens.

3. Copy the model name you selected into the
**IDX > AI: Gemini Model** field.

4. Close the chat window, then re-open it by clicking
spark **Gemini** at
the bottom of the workspace to refresh the model list.


## Next steps

- [Try Gemini in Firebase](https://firebase.google.com/docs/studio/try-gemini).

Was this helpful?



 Send feedback



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Chat


## Ask about this page

bug\_reportfullscreenclose\_fullscreenclose

## Chat

### BETA

restart\_alt

Sign in