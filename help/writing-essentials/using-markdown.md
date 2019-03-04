---
lastModified: 2018-06-28
title: How to use Markdown for writing documentation
seo-title: How to use Markdown for writing Adobe documentation
description: this article provides the basics and reference information for the markdown language used for writing articles.
seo-description: this article provides the basics and reference information for the markdown language used for writing articles for Adobe documentation.
---
# How to use Markdown for writing technical documentation

Adobe technical documentation articles are written in a lightweight markup language called [Markdown](https://daringfireball.net/projects/markdown/), which is both easy to read and easy to learn. 

As we are storing Adobe Docs content in GitHub, it can use a version of Markdown called [GitHub Flavored Markdown (GFM)](https://help.github.com/categories/writing-on-github/), which provides additional functionality for common formatting needs. Additionally, Adobe extended Markdown in a few ways to support certain help-related features such as notes, tips, and embedded videos.

## Markdown basics

### Headings

To create a heading, use a hash mark (#) at the beginning of a line:

```
   # This is level 1 (article title)
   ## This is level 2
   ### This is level 3
   #### This is level 4
   ##### This is level 5
```

### Basic text

A paragraph requires no special syntax in Markdown.

To format text as **bold**, you enclose it in two asterisks. To format text as *italic*, you enclose it in a single asterisk:

```markdown
    This text is **bold**.
    This text is *italic*.
    This is text is both ***bold and italic***.
```

<!--
To format superscript (H<sub>2</sub>O) and subscript (e=mc<sup>2</sup>) text:

```markdown
This is subscript H<sub>2</sub>O and superscript e=mc<sup>2</sup>.
```
-->

To ignore Markdown formatting characters, use \ before the character:

```markdown
This is not \*italicized\* type.
```

### Numbered lists and bullet lists

To create numbered lists, begin a line with 1. or 1), but don't use both formats within the same list, or you'll start a new list. You don't need to specify the numbers. GitHub does that for you.

```markdown
1. This is step 1.
1. This is the next step.
1. This is yet another step, the third.
```

Displayed:

1. This is step 1.
1. This is the next step.
1. This is yet another step, the third.

<!-- markdownlint-disable MD037 -->
To create bullet lists, begin a line with \* or - or +, but don't mix the formats within the same list. (If you mix the formats, such as \* and \+, you essentially start a new list.)
<!-- markdownlint-disable MD037 -->

```markdown
- First item in an unordered list.
- Another item.
- Here we go again.
```

Displayed:

- First item in an unordered list.
- Another item.
- Here we go again.

You can also embed lists within lists and add content between list items.

```markdown
1. Set up your table and code blocks.
1. Perform this step.

   ![screen](assets/no-localize/adobe_standard_logo.png)
1. Make sure that your table looks like this: 

    | Hello | World |
    |---|---|
    | How | are you? |  
1. This is the fourth step.

   >[!NOTE]
   >
   >This is note text.
1. Do another step.
```

Displayed:

1. Set up your table and code blocks.
1. Perform this step.

   ![screen](assets/no-localize/adobe_standard_logo.png)
1. Make sure that your table looks like this: 

    | Hello | World |
    |---|---|
    | How | are you? |  
1. This is the fourth step.

   >[!NOTE]
   >
   >This is note text.
1. Do another step.

### Tables

Tables are not part of the core Markdown specification, but Adobe supports them to an extent. Markdown doesn't support multiple lines lists in cells. Best practice is to avoid using multiple lines in tables. You can create tables by using the pipe (|) character to delineate columns and rows. Hyphens create each column's header, while pipes separate each column. Include a blank line before your table so it's rendered correctly.

```markdown
| Header | Another header | Yet another header |
|------------|:---------------:|-----------------------:|
| row 1 | centered column 2 | right-aligned column 3 |
| row 2 | row 2 column 2 | row 2 column 3 |
```

Displayed:

| Header | Another header | Yet another header |
|------------|:---------------:|-----------------------:|
| row 1 | centered column 2 | right-aligned column 3 |
| row 2 | row 2 column 2 | row 2 column 3 |

Simple tables work adequately in Markdown. However, tables that include multiple paragraphs or lists within a cell are difficult to work with. For such content, we recommend using a different format, such as headings & text.

For more information on creating tables, see:

- GitHub's [Organizing information with tables](https://help.github.com/articles/organizing-information-with-tables/)
- The [Markdown Tables Generator](https://www.tablesgenerator.com/markdown_tables) web app
- [Convert HTML tables to Markdown](https://jmalarcon.github.io/markdowntables/)

### Links

The Markdown syntax for an inline link consists of the `[link text]` portion, which is the text that will be hyperlinked, followed by the `(file-name.md)` portion, which is the URL or file name that's being linked to:

 `[link text](file-name.md)`

```markdown
[Adobe](https://www.adobe.com) or <https://www.adobe.com>
```

Displayed:

[Adobe](https://www.adobe.com) or <https://www.adobe.com>

For links to articles (cross-references) within the repository, use relative links. You can use all relative link operands, such as ./ (current directory), ../ (back one directory), and ../../ (back two directories).

```markdown
See [Overview example article](../../overview.md)
```

For more information on linking, see the [Links](linking.md) article of this guide for linking syntax.

### Images

```markdown
![Adobe Logo](assets/no-localize/adobe_standard_logo.png "Hover text")
```

Displayed:

![Adobe Logo](assets/no-localize/adobe_standard_logo.png "Hover text")

### Code blocks

Markdown supports the placement of code blocks both inline in a sentence and as a separate "fenced" block between sentences. For details, see [Markdown's native support for code blocks](https://daringfireball.net/projects/markdown/syntax#precode)

Use back ticks ( \` ) to create inline code styles within a paragraph. To create a specific multi-line code block, add three back ticks (\`\`\`) before and after the code block (called a "fenced code block" in Markdown and just a "code block" component in AEM). For fenced code blocks, add the code language after the first set of back ticks so that Markdown correctly highlights code syntax. Example: \`\`\`javascript

Examples:

```markdown
This is `inline code` within a paragraph of text.
```

Displayed:

This is `inline code` within a paragraph of text.

This is a fenced code block:

```markdown
\```javascript
function test() {
 console.log("notice the blank line before this function?");
\```
```

Displayed:

```javascript
function test() {
 console.log("notice the blank line before this function?");
```

You can specify properties for code blocks to turn off line numbers (on by default) or add a line wrap (off by default). Use {line-numbers="no"} and {line-wrap="yes"}. These properties are custom Markdown extensions.

\`\`\`javascript {line-numbers="no"}
function test() {
 console.log("notice the blank line before this function?");
\`\`\`

### Definition Lists

A definition list is a Markdown extension that supports the Definition List component in AEM. A definition list consists of a term and its definition.

<!--

```markdown
Frog
: An amphibious green creature. Likes flies.

Cat
: A less amphibious creature than frogs.
```

Displayed:

Frog
: An amphibious green creature. Likes flies.

Cat
: A less amphibious creature than frogs.
--->

#### Remarks and comments

Comments (remarks) do not appear in the public-facing help articles. However, comments do appear in the public-facing Markdown files that users can see and edit.

## Custom Markdown extensions

Adobe articles use standard Markdown for most article formatting, such as paragraphs, links, lists, and headings. For richer formatting, articles can use extended Markdown features such as:

- Note blocks
- Embedded videos
- Do not localize
- Component properties, such as assigning a different heading ID to a heading

Use the Markdown block quote ( > ) at the beginning of every line to tie together an extended component, such as a note. If you need to use subcomponents within components, add an extra level of block quotes (>  >) for that subcomponent section. For example, a NOTE within a DONOTLOCALIZE section should begin with >    >.

Some common Markdown elements such as headings and code blocks include extended properties. If you need to change default properties, add the parameters in french braces /{ /} after the component. Extended properties are described in context.

### Note blocks

You can choose from four types of note blocks to draw attention to specific content:

- `[!NOTE]`
- `[!CAUTION]`
- `[!TIP]`
- `[!IMPORTANT]`

In general, note blocks should be used sparingly because they can be disruptive. Although they also support code blocks, images, lists, and links, try to keep your note blocks simple and straightforward.


```markdown
>[!NOTE]
>This is a standard NOTE block.
```

Displayed:

>[!NOTE]
>This is a standard NOTE block.

```markdown
>[!TIP]
>This is a standard tip.
```

Displayed:

>[!TIP]
>This is a standard tip.

### Videos

Embedded videos won't natively render in Markdown, but you can use this Markdown extension.

```markdown
>[!VIDEO](https://www.youtube.com/watch?v=A0EcD2AxvJE)
```

Displayed:

>[!VIDEO](https://www.youtube.com/watch?v=A0EcD2AxvJE)

### More Like This

The "More Like This" component in AEM appears at the end of an article. It displays related links. When the article is rendered, it can be formatted the same as level-2 headings (##) without being added to the mini-TOC.

<!--
```markdown
>[!MORE]
>* [Article 1](https://helpx.adobe.com/support/analytics.html)
>* [Article 2](https://helpx.adobe.com/support/audience-manager.html){target="new-window"}
```

Displayed:

>[!MORE]
>* [Article 1](https://helpx.adobe.com/support/analytics.html)
>* [Article 2](https://helpx.adobe.com/support/audience-manager.html){target="new-window"}
-->

### DNL - Do Not Localize - and UICONTROL

In some cases, we need to flag certain sections of content within an article to be English only. 
Words, phrases and other elements need to be declared to our translation systems, and creates the ability to manage a controlled lexicon.

For words or phrases that should not be localized, use the `[!DNL]` extension to wrap the word or section.

For elements in the user interface and menus of a solution, we use the `[!UICONTROL]` extension.

**Example:**

In [!DNL Adobe Target] you can create your tests directly on a [!DNL Target]-enabled page.

**Source:**

```markdown
In [!DNL Adobe Target] you can create your tests directly on a [!DNL Target]-enabled page.
```

**Example**

Use the [!UICONTROL Visual Experience Composer] in [!DNL Target] to create your test directly on a page.

**Source:**

```markdown
Use the [!UICONTROL Visual Experience Composer] in [!DNL Target] to create your test directly on a page.
```

## Gotchas and troubleshooting

### Alt text

Alt text that contains underscores won't be rendered properly. For example, instead of using this:

```markdown
![Settings_Step_2] (/assets/settings_step_2.png)
```

OUr best practice is to use hyphens (-) instead of underscores (_) in filenames.

```markdown
![Settings-Step-2] (/assets/settings-step-2.png)
```

### Apostrophes and quotation marks

If you copy text into a Markdown editor, the text might contain "smart" (curly) apostrophes or quotation marks. These need to be encoded or changed to basic apostrophes or quotation marks. Otherwise, you end up with odd characters like this when the file is published: Itâ€™s

Here are the encodings for the "smart" versions of these punctuation marks:

- Left (opening) quotation mark: `&#8220;`
- Right (closing) quotation mark: `&#8221;`
- Right (closing) single quotation mark or apostrophe: `&#8217;`
- Left (opening) single quotation mark (rarely used): `&#8216;`

### Angle brackets

If you use angle brackets in text (not code) in your file--for example, to denote a placeholder--you need to manually encode the angle brackets. Otherwise, Markdown thinks that they're intended to be an HTML tag.

For example, encode `<script name>` as `&lt;script name&gt;`

### Ampersands in titles

Ampersands (&) aren't allowed in titles. Use "and" instead, or use the `&amp;` encoding.

## See also

### Markdown resources

- [Introduction to Markdown](https://daringfireball.net/projects/markdown/syntax)
- [GitHub's Markdown Basics](https://help.github.com/articles/markdown-basics/)
