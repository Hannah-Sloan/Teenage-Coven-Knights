# [Teenage Coven Knights](https://hannah-sloan.github.io/Teenage-Coven-Knights/)



## What Is This?

This project is a TTRPG presented not through pdf, but **html**. I write the game system in markdown and then convert the markdown to HTML. You can check it out the at the link above, or browse the raw files here on github.

I'll use the github side of the project to document the development and my html design goals. I'm hoping to find a way to showcase my game design philosophy within the TTRPG somewhere, rather than here. 

## Style Constraints

I am brand new to HTML and CSS, so I have a number of constraints placed on the project so that it 1) does not get out of hand for my skill and 2) Has a cohesive style in its simplicity.

I am interested in making a truly HTML presented SRD, but this is not that project. My first constraint is that the game **only contains things I can do in markdown**. HTML is much more powerful than markdown, but this way I can potentially still create a PDF version as well.

### Accessibility

The rest are accessibility constraints in a hope that having a web version of an rpg could make it *more* accessible, despite the additional requirement for technology. If you have *any* accessibility concerns feel free to *create an issue* on Github and I will attempt to address it!

Documents should be **readable on all devices, resolutions, and text sizes.**

Following WCAG 2.1 as much as possible, ensuring easy readability and supporting screen readers.

<u>A few examples:</u>

-  Sections have headings that identify them: A correct **reading sequence can be programmatically determined**.
- Color is not used as the only visual means of conveying information.
- The visual presentation of text and images of **text has a contrast ratio of at least 4.5:1**.
- Text can be resized without assistive technology **up to 200 percent** without loss of content or functionality.
- Text is not justified.
- Line spacing is at least **space-and-a-half within paragraphs**, and paragraph spacing is at least 1.5 times larger than the line spacing.
- Web pages have **titles** that describe topic or purpose.
- The purpose of each link can be determined from the **link text alone**.

## Game License

You may **not** use the game's art. You may **only** use Logos and images included in the Creator Kit.

The **text** of Teenage Coven Knights is Licensed under the [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/legalcode). This allows you to copy Teenage Coven Knights into any medium or format, and to remix, transform, and build upon the text so long as you **do not** use the material for commercial purposes and you include the following:

**Attribution Statement:**

*"(Content Title) draws from **Teenage Coven Knights** by **Hannah Ava Sloan** which is available at https://hannah-sloan.github.io/Teenage-Coven-Knights/ and is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International** available at https://creativecommons.org/licenses/by-nc/4.0/. Such Licensed Material [has/has not] been modified."*

### **Third-Party Content**

The License refers to the sharing and transformation of the Teenage Coven Knights RPG. Third-Party content that does **not contain** anything within The Teenage Coven Knights RPG is not restricted by the License. That means **you are free to:**

1)  Use the general rules and **game mechanics** of Teenage Coven Knights. 
2)  State your content is **"Teenage Coven Knights compatible"**.
3)  Use your content for **commercial purposes**. 

Additionally you may **Reference** Teenage Coven Knights' original people, places, items, creatures, spells, and features. **So long as** you include the following in your content:

*"[Content Title] is Third-Party Content and is **not** affiliated with Hannah Ava Sloan, Teenage Coven Knights, or its creators."*

### Open Source

This project's code is publicly available here on this Github. Redistributing the project in its entirety or any of the markdown or html falls under the Game License, since the source code contains the verbatim text of the RPG. Fortunately, the License allows you to copy, remix, transform, and build on the text so long as you **include the attribution statement**. Make sure you **remember this step** when creating ***forking or cloning*** of the repository!

The hope is this will allow you to easily create **Teenage Coven Knights hacks**, as well as create *Pull requests* with community suggestions or just improving the code. Though I will retain control of this version of Teenage Coven Knights it's the **community that will drive it** to be the best it can be. Perhaps a popular fork will completely open source development- containing popular rule variations and homebrew! You could steal the css style and use it to present your homebrew class (see **Third-Party Content** above). The process of writing for linked markdown pages is different than for pdf; perhaps you want to use this github as a template to converting your markdown project to html. This github is meant to **allow you** to do all of that.

## Special Markdown Syntax

In creating this SRD I wanted features native markdown didn't support. This is one reason why I made my own markdown to html converter (markdownToHtml.py). That means I can support a few extra tricks:

### Linking to a specific section

Simply add a link like usual but include #your-header-lower-case-dashes for example: 

```
[Link Text](#resting-and-healing)
```

This works for sections in other files too, just specify the file first

```
[Link Text](game_rules.md#resting-and-healing)
```

NOTE: You cannot link to h1 headers (titles). This functionality should be covered just by linking to the file itself. The .md in the link will automatically be converted to .html when the markdown is converted to html

### No starting with

I search for links and images by searching for *'!['* and then searching for *'['* so your regular text cannot include those unless you are making a link or image. Same goes for *'\*'* for bold and italics.

## TODO

- ~~Local links (within a file *and to other sections!*)~~
- 'Embeds'
- 'Tooltips' (defined terms)
- Search Function