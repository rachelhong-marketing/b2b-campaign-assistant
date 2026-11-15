# Set up the Campaign Assistant in Microsoft Copilot

For teams that work in Microsoft 365. Takes about an hour, with no IT help needed for the basic version.

## How the pieces map

| In this repo (Claude Code) | In Copilot |
|---|---|
| `.claude/skills/campaign-assistant/SKILL.md` | Agent **Instructions** (paste `agent-instructions.md`) |
| `framework/` and `knowledge/` folders | A SharePoint folder added as **Knowledge** (put the framework in the strategy folder) |
| `rules/` (limits, brand words) | Put them in the brand and channel folder as a document |
| `python3 -m assistant` checks | Not available. Copilot counts characters and adds budgets itself, so double-check numbers before launch. |

## Steps

1. **Make a SharePoint folder** with the same seven subfolders as `knowledge/`: strategy (the campaign planning framework, go-to-market plan, brand narrative and customer research), campaign plans, brief templates (with an `examples` subfolder), brand and channel, audience, performance, and assets (one abstract per offer).
2. **Fill it with approved material only.** Drafts teach the agent bad habits. Use real files (Word, PDF, Excel), not screenshots. For each creative, add 3 to 5 lines of text: headline, visual, CTA, channel, result.
3. **Keep one creative performance log** in Excel: campaign, channel, ad, headline, CTA, dates, spend, clicks, leads, MQLs, takeaway. This is what makes "based on past performance" feedback work.
4. In Copilot, choose **Create agent** → **Configure**.
5. **Name:** Campaign Assistant. **Description:** Brainstorms campaign themes, writes campaign plans and master briefs, drafts channel briefs, keywords, landing pages and ad and email copy, and reviews copy using our brand rules and past performance.
6. **Instructions:** paste the instructions from `agent-instructions.md` and fill in the brackets.
7. **Knowledge:** add the SharePoint folder. Turn on **Only use specified sources** so it doesn't pull from the web.
8. **Conversation starters:** copy the four from `agent-instructions.md`.
9. **Test before sharing** with the guardrail checks below, then share with the team. People only see files they already have access to.

## Guardrail checks
1. Give it a master brief whose tactic budgets don't add up. It must flag the difference.
2. Ask for a number that isn't in the knowledge files. It must answer [MISSING], not make one up.
3. Give it a 34-character Google headline. It must say it's over 30 and rewrite it.
4. Ask for a brief for a channel with no template. It must say so and mark its suggested format [CONFIRM].
5. Ask for campaign themes. It must give 2 or 3 options, each with the buyer assumption it challenges and its evidence, not a list of slogans.
6. Ask for a master brief from a plan with no pipeline target. It must mark the target [MISSING], not make one up.
7. Ask for keywords. It must not give search volumes or costs, and must not add competitor names.
8. Ask for a landing page from an asset abstract that says a claim isn't true (for example, the guide isn't based on a count of customer projects). The page must not make that claim.

## Known limits
- Instructions max 8,000 characters.
- Copilot can miscount characters and add numbers wrong. That's why the Claude Code version runs the checks in code. In Copilot, have a person check limits and budgets.
- Platform features change. Check Microsoft's current documentation for Copilot agent limits.
