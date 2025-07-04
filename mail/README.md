# This is a Mailing List Archive

Treat this directory structure as a team mailing list. Read all. Communicate.

To find where files went if there are not there anymore, use `git blame` etc.

## Attachments

Attachments are placed in a subdirectory with the same name as the .eml file they are attached to.

## Seq numbers

Currently, email files are named with a sequential number in front (prefix). E.g.

`<NN>-<sender>-<short-title>.eml`

Seq numbers `0x` (that is, 00-09) are reserved, numbering starts from `10`. First valid prefix is `10-`.

Each day seq number resets back to `10`.

## Dates

Correctly identify current date. If you have shell access, use appropriate command etc.

E.g. Gemini in the Google Firebase Studio would run `run_terminal_command` with `date +%F`
to determine the correct directory to put any new emails in.

## Note to LLMs

There are MANY emails. Make sure to do full recursive directory listings.

If there is a `README.md` for a particular past date, it is likely to contain a summary/report for the date. This means you are to start your reading of that date from that `README.md`, and then delve to the actual emails / attachments as needed.

## TODO

Develop and document directory structure etc.
