# LIFEOS — API KEYS AND EXTERNAL SERVICES

## 1. Purpose

This document tracks every external API, credential, OAuth application and third-party service used by LIFEOS.

The application must not depend on every service being configured.

Each integration must have:
- A clear purpose.
- A configuration status.
- Environment variable names.
- Setup instructions.
- Free-tier or local alternatives where available.
- Graceful behavior when unavailable.

Never commit actual secrets to Git.

Never put API keys in frontend environment variables.

---

## 2. AI AND LANGUAGE MODEL PROVIDERS

### OpenAI API

- Purpose: LLM responses, agent orchestration and intelligent workflows.
- Environment variables:
  - `OPENAI_API_KEY`
  - `OPENAI_MODEL`
- Required: Only if OpenAI is selected as the active LLM provider.
- Website: https://platform.openai.com/api-keys

### Groq API

- Purpose: Fast LLM inference.
- Environment variables:
  - `GROQ_API_KEY`
  - `GROQ_MODEL`
- Required: Only if Groq is selected.
- Website: https://console.groq.com/keys

### Google Gemini API

- Purpose: Alternative LLM provider.
- Environment variables:
  - `GOOGLE_API_KEY`
  - `GEMINI_MODEL`
- Required: Optional.
- Website: https://aistudio.google.com/apikey

**Implementation requirement:** Implement a configurable LLM provider abstraction. Only one provider needs to be configured for normal AI functionality. Do not require all three.

---

## 3. GOOGLE CALENDAR AND GMAIL

### Google Cloud OAuth

- Purpose:
  - Google Calendar synchronization.
  - Gmail access.
  - Email intelligence.
- Environment variables:
  - `GOOGLE_CLIENT_ID`
  - `GOOGLE_CLIENT_SECRET`
  - `GOOGLE_REDIRECT_URI`
  - `GOOGLE_SCOPES`

Setup:

1. Visit https://console.cloud.google.com/
2. Create a Google Cloud project.
3. Enable Gmail API.
4. Enable Google Calendar API.
5. Configure OAuth consent.
6. Create OAuth 2.0 credentials.
7. Configure the authorized redirect URI.
8. Add credentials to the backend `.env`.

Required: Only for real Gmail and Google Calendar integrations.

Local task and calendar functionality must work without these credentials.

Use minimum necessary OAuth scopes.

Store OAuth tokens securely and support token refresh and revocation.

---

## 4. DOCUMENT PROCESSING AND EMBEDDINGS

### Local embedding models

- Purpose: Document vectorization and RAG.
- Suggested model: `sentence-transformers/all-MiniLM-L6-v2`.
- API key: Not required.
- Environment variable:
  - `EMBEDDING_MODEL`

### Optional hosted embeddings

Possible providers:
- OpenAI.
- Google Gemini.

Required: No, if local embeddings are implemented.

### Vector storage

Preferred options:
- FAISS for local development.
- PostgreSQL with pgvector for production-oriented deployment.

API key: Not required for local FAISS.

---

## 5. INVESTMENT AND MARKET DATA

Implement a provider abstraction.

Possible providers:

### Alpha Vantage
- Purpose: Stock market data.
- Environment variable: `ALPHA_VANTAGE_API_KEY`
- Website: https://www.alphavantage.co/support/#api-key
- Required: Optional.

### Financial Modeling Prep
- Purpose: Company information and financial data.
- Environment variable: `FMP_API_KEY`
- Website: https://site.financialmodelingprep.com/
- Required: Optional.

### Alternative market-data provider
The agent should evaluate available free-tier providers and document the selected provider, its rate limits and supported markets.

Important:
- Never fabricate market prices.
- Clearly identify delayed data.
- Do not assume free plans provide unrestricted live Indian market data.
- Allow manual portfolio updates.

---

## 6. NOTIFICATION SERVICES

### Email notifications

Possible implementation:
- SMTP.
- Resend.

Environment variables:

- `SMTP_HOST`
- `SMTP_PORT`
- `SMTP_USERNAME`
- `SMTP_PASSWORD`
- `SMTP_FROM_EMAIL`

Optional Resend:

- `RESEND_API_KEY`

Website: https://resend.com/

Required: No, for core in-app notifications.

### Telegram notifications

Optional enhancement.

Environment variables:

- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`

Website: https://core.telegram.org/bots

Required: No.

---

## 7. OPTIONAL FILE STORAGE

For local development:

- Local filesystem storage.
- No API key required.

For cloud deployment:

Possible providers:
- Cloudflare R2.
- Amazon S3.

Environment variables:

- `STORAGE_PROVIDER`
- `S3_ENDPOINT_URL`
- `S3_BUCKET_NAME`
- `S3_ACCESS_KEY_ID`
- `S3_SECRET_ACCESS_KEY`
- `S3_REGION`

Required: No, if local storage is implemented.

---

## 8. OPTIONAL OCR

For extracting text from scanned documents:

Possible tools:
- Tesseract OCR.
- OCR-capable hosted APIs.

Local Tesseract does not require an API key.

Use OCR only when ordinary document text extraction is insufficient.

---

## 9. DATABASE AND SECURITY CONFIGURATION

### PostgreSQL

Environment variable:

- `DATABASE_URL`

Example placeholder:

`postgresql+psycopg://USER:PASSWORD@HOST:5432/lifeos`

Required: Depends on the selected database configuration.

### Authentication

Environment variables:

- `SECRET_KEY`
- `ACCESS_TOKEN_EXPIRE_MINUTES`
- `REFRESH_TOKEN_EXPIRE_DAYS`

Generate a cryptographically secure secret locally.

Never commit actual secret values.

### Application configuration

Suggested variables:

- `APP_ENV`
- `DEBUG`
- `FRONTEND_URL`
- `BACKEND_URL`
- `CORS_ORIGINS`
- `TIMEZONE`

---

## 10. INITIAL CREDENTIAL CHECKLIST

| Integration | API key required? | Priority |
|---|---|---|
| One selected LLM provider | Yes | Required for AI |
| Google OAuth | Yes | Optional integration |
| Local embeddings | No | Recommended |
| FAISS | No | Recommended |
| PostgreSQL | Credentials/config | Production database |
| Alpha Vantage | Yes | Optional |
| Financial Modeling Prep | Yes | Optional |
| SMTP/Resend | Yes | Optional |
| Telegram | Yes | Optional |
| Local file storage | No | Recommended |
| Tesseract OCR | No API key | Optional |

---

## 11. CONFIGURATION RULES

The coding agent must:

1. Create `.env.example` containing every required environment variable.
2. Create a real `.env` only when appropriate, with placeholders or safe defaults rather than fabricated credentials.
3. Add `.env` to `.gitignore`.
4. Validate required configuration during application startup.
5. Distinguish missing optional credentials from fatal configuration errors.
6. Display integration connection status in the settings interface.
7. Document the exact setup procedure for each integration.
8. Never expose backend credentials to React.
9. Never log API keys, passwords or OAuth tokens.
10. Support disconnecting and reconnecting integrations.
11. Update this document whenever a new external dependency is introduced.
12. Identify any paid API, usage-based billing or restrictive free-tier limitation before depending on it.

## 12. FINAL INTEGRATION REPORT

At project completion, replace the initial checklist with the actual implementation status.

For every provider, document:

- Implemented or not implemented.
- Environment variables.
- Setup URL.
- Free-tier availability.
- Pricing or usage limitations.
- Features dependent on it.
- Local fallback.
- Tested or untested.

**The goal is to make LIFEOS usable with minimal external credentials while allowing integrations to be enabled progressively.**