# gmail-no-send

A **drafts-only** Gmail client (CLI + library) designed for AI-agent safety. It supports **read, search, draft creation/update, and archiving** — **no send** code paths exist.

Use this when you want to guarantee at the application layer that nothing can send emails, while still allowing drafts for human review.

## Features

- Search inbox threads/messages
- Read messages
- Create and update drafts
- Archive messages (remove INBOX label)
- **No send implementation** (no API calls to `users.messages.send` or `users.drafts.send`)
- Audit log (JSONL) for every action

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Setup OAuth

1. Create OAuth credentials in Google Cloud Console (Desktop app)
2. Download `client_secret_*.json`
3. Run auth:

```bash
gmail-no-send auth --client-secret /path/to/client_secret.json --account you@gmail.com
```

Tokens are stored at: `~/.config/gmail-no-send/token.json`

## CLI Usage

```bash
# search threads
gmail-no-send search --account you@gmail.com --query "is:unread" --max 10

# read a message
gmail-no-send read --account you@gmail.com --message-id <id>

# create draft
gmail-no-send draft-create --account you@gmail.com --to someone@example.com --subject "Hello" --body-file ./message.txt

# update draft
gmail-no-send draft-update --account you@gmail.com --draft-id <id> --subject "Updated" --body-file ./message.txt

# archive
gmail-no-send archive --account you@gmail.com --message-id <id>
```

## Library

```python
from gmail_no_send import GmailNoSend

client = GmailNoSend(account="you@gmail.com")
client.search("is:unread", max_results=5)
client.create_draft(to="a@b.com", subject="Hi", body="Hello")
```

## Threat model (explicit)

- This tool **prevents sending in its own code**.
- It does **not** prevent a user from using other Gmail clients or the Gmail UI to send.
- OAuth scopes can’t prevent sending if `gmail.compose` is granted; this tool simply never calls send endpoints.

## License

MIT
