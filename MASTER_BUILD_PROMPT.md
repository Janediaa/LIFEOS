# LIFEOS — COMPLETE END-TO-END MASTER BUILD SPECIFICATION

## 1. YOUR ROLE

You are the Principal Software Architect, Senior Full-Stack Engineer, AI/ML Engineer, Database Engineer, DevOps Engineer, Security Engineer, QA Engineer and UI/UX Designer responsible for completing LIFEOS.

You are not building a prototype, a landing page, a chatbot demo or a collection of disconnected CRUD pages.

You are building a fully functional, integrated, reliable Personal AI Operating System.

Your responsibility is to inspect the existing repository, understand its architecture, preserve working implementations, identify incomplete functionality, implement every feature, integrate all modules, run tests, fix failures and deliver a working application.

**Do not stop at planning. Execute the implementation.**

Do not declare a feature complete merely because:
- A page exists.
- A button is visible.
- An API endpoint returns HTTP 200.
- Mock data appears on the dashboard.
- A chatbot produces a response.
- A database table has been created.

Every feature must work through its actual frontend, backend, database and integration layers.

---

# 2. PROJECT OBJECTIVE

LIFEOS is a centralized personal management platform that allows an individual to manage their digital life through one application and one conversational AI interface.

The application must integrate:

1. Personal finance management.
2. Expense and income tracking.
3. Budgeting and financial analytics.
4. Insurance and policy management.
5. Bills and subscription tracking.
6. Investment research and portfolio analytics.
7. Google Calendar integration.
8. Task and project management.
9. Gmail intelligence.
10. Document management and RAG.
11. Persistent personal AI memory.
12. Habits and routines.
13. Goal management.
14. Proactive monitoring and notifications.
15. Multi-agent conversational AI.
16. Unified search and personal knowledge retrieval.
17. Personal analytics and an intelligent dashboard.

All modules must share a common identity, database architecture, permission model and AI context layer.

The user should be able to manage information manually, through dedicated interfaces, through connected services and through natural-language conversations.

---

# 3. FIRST: AUDIT THE EXISTING REPOSITORY

Before modifying anything, inspect the entire repository.

Do not assume the existing architecture is incorrect. Do not rewrite functioning components unnecessarily.

Inspect:

- Root directory and folder structure.
- Frontend framework, routing and components.
- Backend framework, API routes and service layers.
- Database configuration and existing models.
- Alembic migrations.
- Authentication and authorization.
- Existing AI agents and LLM integrations.
- Existing integrations and API clients.
- Environment variables and configuration.
- Dependency files.
- Existing tests.
- Git branches, commits and uncommitted changes.
- Existing documentation.
- Frontend and backend execution commands.

Determine:

1. What already works.
2. What is partially implemented.
3. What is broken.
4. What is missing.
5. Which components can be reused.
6. Which architectural changes are necessary.

Create:

`docs/IMPLEMENTATION_AUDIT.md`

Document the actual state of the repository.

**Critical preservation rules:**

- Never blindly overwrite existing working files.
- Never delete existing functionality without a justified replacement.
- Never reset Git history.
- Never execute destructive database operations against existing user data.
- Never modify unrelated project directories.
- Never introduce a second competing implementation of an existing service.
- Never silently change API contracts relied upon by the frontend.

After the audit, establish a phased implementation plan and begin executing it.

Do not wait for additional approval for ordinary engineering decisions.

---

# 4. REQUIRED TECHNOLOGY AND ENGINEERING STANDARDS

Preserve the existing working stack wherever practical.

Preferred architecture:

### Frontend
- React.
- Vite.
- TypeScript where feasible, while respecting existing project conventions.
- Tailwind CSS or the existing styling framework.
- React Router.
- TanStack Query for server state.
- Zustand or an equivalent lightweight state-management solution.
- Reusable component architecture.
- Accessible, responsive layouts.

### Backend
- Python.
- FastAPI.
- Pydantic.
- SQLAlchemy 2.x.
- Alembic.
- Async operations where they provide meaningful benefits.
- Modular service and repository layers.
- Structured exception handling.
- Background jobs for scheduled and long-running tasks.

### Database
- PostgreSQL as the preferred production database.
- Preserve an existing working database configuration where changing it would cause unnecessary disruption.
- SQLite may be supported for lightweight local development if the architecture permits it.
- Proper foreign keys, constraints, indexes and transactions.

### AI infrastructure
- LangChain and LangGraph where appropriate.
- Tool-calling LLM architecture.
- RAG with modular embedding providers.
- FAISS or another appropriate vector database for local development.
- PostgreSQL with pgvector as an optional production-oriented alternative.
- Configurable model providers.

Do not introduce frameworks simply because they are popular.

Every dependency must have a purpose.

### Development environment rules

These are mandatory:

- Python dependency management: `uv`.
- Frontend dependency management: `npm`.
- Terminal: Git Bash on Windows.
- Python commands must use `uv run`.
- Add dependencies using `uv add`.
- Remove dependencies using `uv remove`.
- Synchronize using `uv sync`.
- Never rely on globally installed Python packages.
- Do not require manual virtual environment activation.
- Do not use pip as the normal dependency-management workflow.

Maintain a clean, reproducible development environment.

---

# 5. APPLICATION ARCHITECTURE

Implement a modular architecture with clear separation between:

1. Frontend presentation.
2. Backend API layer.
3. Business logic.
4. Data access.
5. AI orchestration.
6. External integrations.
7. Background workers.
8. Notification delivery.
9. Authentication and authorization.

Suggested backend organization (adapt to the existing repository):

backend/app/
- api/
  - routes/
  - dependencies.py
- core/
  - config.py
  - security.py
  - logging.py
  - exceptions.py
- models/
- schemas/
- repositories/
- services/
- agents/
- integrations/
  - llm/
  - google/
  - finance/
  - market_data/
  - notifications/
- workflows/
- workers/
- utils/
- main.py

Suggested frontend organization:

frontend/src/
- app/
- components/
- layouts/
- pages/
- features/
  - dashboard/
  - finance/
  - insurance/
  - investments/
  - calendar/
  - tasks/
  - email/
  - documents/
  - memory/
  - habits/
  - goals/
  - notifications/
  - assistant/
- hooks/
- services/
- stores/
- types/
- utils/

These are architectural guidelines, not permission to reorganize the entire working repository unnecessarily.

---

# 6. COMPLETE FEATURE REQUIREMENTS

## MODULE A — PERSONAL DASHBOARD

Build a comprehensive dashboard that serves as the application's central command center.

Display:

- Total financial balance.
- Income and expenses.
- Monthly savings.
- Budget utilization.
- Upcoming bills.
- Upcoming calendar events.
- Pending tasks.
- Habit completion.
- Active goals.
- Investment portfolio summary.
- Important emails.
- Document activity.
- AI-generated daily briefing.
- Alerts and reminders.

Requirements:

- Real database-backed information.
- Customizable dashboard widgets.
- Date-range filters.
- Useful empty states.
- Loading and error states.
- Refresh and synchronization indicators.
- Quick actions.
- Responsive design.

Do not populate the dashboard with fake numbers when real user data is unavailable.

Show meaningful empty states instead.

## MODULE B — PERSONAL FINANCE MANAGEMENT

Build a complete personal finance management module.

### Income and expenses

Users must be able to:

- Add income.
- Add expenses.
- Edit and delete transactions.
- Categorize transactions.
- Add custom categories.
- Add transaction descriptions and notes.
- Record transaction dates.
- Track payment methods.
- Attach receipts.
- Filter and search transactions.
- Import transactions from CSV.
- Export transaction records.

### Financial analytics

Calculate:

- Total income.
- Total expenses.
- Net savings.
- Savings rate.
- Monthly trends.
- Category-wise spending.
- Month-over-month comparisons.
- Cash flow.
- Spending patterns.

All calculations must use actual transaction records.

### Budgeting

Implement:

- Monthly budgets.
- Category budgets.
- Budget limits.
- Spending progress.
- Budget alerts.
- Overspending notifications.
- Budget history.

### Accounts

Support multiple manually maintained accounts:

- Bank accounts.
- Cash.
- Savings accounts.
- Credit cards.
- Other financial accounts.

Allow balance adjustments with proper transaction history.

Do not store banking passwords or raw banking credentials.

Provide CSV imports and a provider abstraction for future financial integrations.

## MODULE C — INSURANCE AND POLICY MANAGEMENT

Users must be able to manage:

- Health insurance.
- Life insurance.
- Vehicle insurance.
- Travel insurance.
- Other policies.

Each policy should support:

- Provider.
- Policy name.
- Policy number.
- Coverage amount.
- Premium amount.
- Payment frequency.
- Start date.
- Expiry date.
- Renewal date.
- Nominee information.
- Contact information.
- Policy documents.
- Notes.

Implement:

- Renewal reminders.
- Premium payment reminders.
- Expiry alerts.
- Document storage.
- Policy search.
- Policy status tracking.
- Coverage overview.

Sensitive policy information must be protected with appropriate authorization.

## MODULE D — BILLS AND SUBSCRIPTIONS

Allow users to manage recurring financial obligations.

Examples:

- Rent.
- Electricity.
- Internet.
- Mobile bills.
- Insurance premiums.
- OTT subscriptions.
- Software subscriptions.
- Loan payments.

Features:

- Recurrence configuration.
- Due dates.
- Amounts.
- Payment status.
- Renewal dates.
- Reminder scheduling.
- Monthly and annual cost summaries.
- Upcoming payment calendar.
- Mark as paid.
- Payment history.

Do not automatically claim that a payment has been made unless the user or an authorized integration confirms it.

## MODULE E — INVESTMENT RESEARCH AND PORTFOLIO ANALYTICS

Build an investment management and research workspace.

Support manually entered holdings initially.

Features:

- Stocks.
- ETFs.
- Mutual funds.
- Other configurable asset types.
- Holdings.
- Units.
- Purchase price.
- Current price.
- Invested amount.
- Current value.
- Unrealized profit/loss.
- Asset allocation.
- Portfolio performance.
- Transaction history.
- Watchlists.

Investment research:

- Search for securities.
- Retrieve market information through configured providers.
- Display historical price data where available.
- Display company information.
- Track watchlist changes.
- Provide investment research summaries.
- Clearly identify the source and timestamp of financial data.

Important:

- Never fabricate market prices.
- Never display stale data as live data.
- Handle unavailable providers explicitly.
- Distinguish actual financial data from estimates.
- AI-generated investment analysis must not be presented as guaranteed financial advice.
- Support manual portfolio updates when market APIs are unavailable.

## MODULE F — GOOGLE CALENDAR

Implement real Google Calendar OAuth integration.

Users should be able to:

- Connect their Google account.
- View calendar events.
- Create events.
- Update events.
- Delete events.
- View upcoming schedules.
- Search events.
- Check scheduling conflicts.
- Create reminders.
- Synchronize changes.

Support:

- OAuth consent.
- Secure token storage.
- Access token refresh.
- Revocation and disconnect.
- Permission error handling.
- Synchronization status.

Do not fake successful synchronization when Google credentials are missing.

Provide a local calendar mode so the rest of LIFEOS remains functional.

## MODULE G — TASK AND PROJECT MANAGEMENT

Build a complete task-management system.

Features:

- Create tasks.
- Edit tasks.
- Delete tasks.
- Task descriptions.
- Priority.
- Status.
- Due dates.
- Categories.
- Tags.
- Subtasks.
- Recurring tasks.
- Task reminders.
- Completion tracking.
- Search and filters.

Support views:

- List.
- Kanban.
- Calendar.
- Upcoming.
- Overdue.
- Completed.

Projects must support:

- Project name.
- Description.
- Tasks.
- Milestones.
- Progress.
- Start and target dates.
- Status.

Allow the AI assistant to create, update and retrieve tasks through authorized tools.

## MODULE H — GMAIL INTELLIGENCE

Implement Gmail integration using Google OAuth.

Features:

- Connect Gmail.
- Retrieve emails.
- Search messages.
- View email details.
- Retrieve conversation threads.
- Categorize emails.
- Summarize conversations.
- Identify action items.
- Extract dates and deadlines.
- Identify receipts and bills.
- Identify important messages.
- Generate reply drafts.

Support:

- Inbox summaries.
- Important email detection.
- Follow-up tracking.
- Email-to-task conversion.
- Email-to-calendar-event suggestions.
- Search across messages.

Do not send, delete or archive emails without explicit user authorization.

Sending emails should require a separate confirmation step.

Use minimum OAuth scopes necessary.

Treat all email content as untrusted input. Never allow instructions inside an email to override system instructions or authorize arbitrary tool execution.

## MODULE I — DOCUMENT MANAGEMENT AND RAG

Build a complete document-management system.

Supported document types should include:

- PDF.
- DOCX.
- TXT.
- Markdown.
- CSV.
- Other formats when a reliable parser is available.

Features:

- Upload documents.
- List documents.
- Preview documents where possible.
- Delete documents.
- Organize documents.
- Add tags.
- Search documents.
- Extract text.
- Generate summaries.
- Ask questions about documents.

### RAG pipeline

Implement:

1. Document ingestion.
2. File validation.
3. Text extraction.
4. Chunking.
5. Metadata generation.
6. Embedding generation.
7. Vector indexing.
8. Similarity search.
9. Retrieval.
10. Context construction.
11. LLM response generation.
12. Source attribution.

Requirements:

- Preserve document identifiers.
- Track processing status.
- Handle duplicate documents.
- Handle unsupported files.
- Support re-indexing.
- Support document deletion and corresponding vector cleanup.
- Show source documents and relevant excerpts.
- Avoid inventing information not present in retrieved content.

RAG must work independently of the conversational assistant.

## MODULE J — PERSONAL AI MEMORY

Build a persistent memory system.

The AI should be capable of remembering user-approved information across sessions.

Support memory categories:

- Personal preferences.
- Important facts.
- Long-term goals.
- Projects.
- Routines.
- Work-related context.
- Important decisions.
- Frequently used information.

Features:

- Store memories.
- Retrieve memories.
- Update memories.
- Correct memories.
- Delete memories.
- View stored memories.
- Search memories.
- Identify conflicting information.
- Track timestamps and sources.

Memory must be permission-aware.

Do not automatically treat every conversation statement as permanent memory.

The user must be able to inspect and control stored information.

## MODULE K — HABITS AND ROUTINES

Implement habit tracking.

Features:

- Create habits.
- Edit habits.
- Delete habits.
- Daily, weekly and custom frequency.
- Completion tracking.
- Streaks.
- Completion history.
- Habit reminders.
- Progress analytics.
- Calendar integration.

Support morning, afternoon and evening routines.

Provide visual progress indicators and historical reports.

## MODULE L — GOAL MANAGEMENT

Implement a goal-management system.

Support:

- Short-term goals.
- Long-term goals.
- Personal goals.
- Career goals.
- Financial goals.
- Learning goals.
- Health and fitness goals.

Each goal should include:

- Title.
- Description.
- Category.
- Target date.
- Progress.
- Milestones.
- Related tasks.
- Status.

Allow users to break goals into smaller milestones and tasks.

The AI should be able to suggest actionable plans and monitor progress.

## MODULE M — NOTIFICATIONS AND PROACTIVE MONITORING

Build a reliable notification system.

Support:

- In-app notifications.
- Scheduled reminders.
- Upcoming bill alerts.
- Insurance renewal alerts.
- Calendar reminders.
- Task deadline alerts.
- Habit reminders.
- Goal progress notifications.
- Investment watchlist alerts.
- Email follow-up reminders.

Implement:

- Notification preferences.
- Read/unread status.
- Notification history.
- Scheduling.
- Retry handling.
- Duplicate prevention.
- Time-zone awareness.
- Background execution.

Use a proper scheduler or background job system rather than unreliable frontend timers.

Users must be able to disable individual notification categories.

## MODULE N — MULTI-AGENT AI ASSISTANT

This is a core differentiator of LIFEOS.

Build a central conversational assistant backed by a modular agent architecture.

Suggested architecture:

### 1. Supervisor Agent

Responsibilities:

- Understand user intent.
- Classify requests.
- Select the appropriate specialist.
- Coordinate multi-step operations.
- Manage context.
- Validate results.
- Return consolidated responses.

### 2. Finance Agent

Tools:

- Retrieve transactions.
- Add transactions.
- Analyze expenses.
- Retrieve budgets.
- Calculate savings.
- Retrieve financial summaries.

### 3. Calendar Agent

Tools:

- Retrieve events.
- Create events.
- Update events.
- Delete events.
- Check availability.

### 4. Task Agent

Tools:

- Create tasks.
- Retrieve tasks.
- Update tasks.
- Complete tasks.
- Retrieve project progress.

### 5. Email Agent

Tools:

- Search emails.
- Summarize threads.
- Extract action items.
- Create drafts.
- Suggest follow-ups.

### 6. Document Agent

Tools:

- Search documents.
- Retrieve document context.
- Answer questions through RAG.
- Summarize documents.

### 7. Memory Agent

Tools:

- Retrieve relevant memories.
- Store approved memories.
- Update memories.
- Delete memories.

### 8. Habit and Goal Agent

Tools:

- Retrieve habits.
- Record completion.
- Retrieve goals.
- Update goal progress.
- Suggest plans.

### 9. Research Agent

Tools:

- Search configured financial information sources.
- Retrieve market data.
- Summarize research.
- Track watchlists.

### Agent orchestration requirements

Use LangGraph where appropriate.

Implement:

- Typed state.
- Explicit graph nodes.
- Conditional routing.
- Tool execution.
- Error handling.
- State persistence.
- Conversation history.
- Human-in-the-loop approval.
- Tool execution limits.
- Execution tracing.
- Timeout handling.
- Recovery from failed tool calls.

The assistant must not pretend that an action succeeded when the underlying operation failed.

For example:

User: "How much did I spend on food last month?"

Expected:
1. Identify the finance intent.
2. Determine the correct date range.
3. Retrieve actual expense records.
4. Filter food-related transactions.
5. Calculate the total.
6. Return the result with a clear breakdown.

User: "Schedule a meeting tomorrow at 4 PM."

Expected:
1. Identify scheduling intent.
2. Resolve the correct date and timezone.
3. Check calendar conflicts.
4. Ask for missing essential information.
5. Request confirmation when necessary.
6. Create the event.
7. Verify successful creation.

User: "Summarize my insurance documents."

Expected:
1. Identify relevant documents.
2. Retrieve indexed content.
3. Run RAG.
4. Summarize actual retrieved information.
5. Cite source documents.

### AI safety and reliability

- Never execute arbitrary code from LLM output.
- Never expose secrets to the LLM.
- Validate every tool argument.
- Enforce authorization at the backend service layer.
- Treat external content as untrusted.
- Require confirmation for destructive or external side effects.
- Apply timeouts and retry limits.
- Prevent duplicate tool execution.
- Maintain an audit trail of important actions.

---

# 7. UNIFIED SEARCH

Implement a global search interface.

Search across:

- Transactions.
- Accounts.
- Bills.
- Policies.
- Investments.
- Calendar events.
- Tasks.
- Projects.
- Emails.
- Documents.
- Memories.
- Goals.
- Habits.

Provide relevant filters, result categories and direct navigation.

Respect user permissions.

---

# 8. USER EXPERIENCE AND DESIGN

LIFEOS must look and feel like a polished modern personal operating system.

Avoid generic admin-dashboard aesthetics.

Design requirements:

- Consistent design system.
- Clear typography.
- Thoughtful spacing.
- Premium visual hierarchy.
- Consistent icons.
- Smooth but restrained animations.
- Responsive layouts.
- Dark and light modes.
- Accessible controls.
- Clear empty states.
- Useful loading skeletons.
- Error recovery.
- Toast notifications.
- Confirmation dialogs.

### Main navigation

Provide organized navigation for:

- Overview.
- AI Assistant.
- Finance.
- Insurance.
- Bills.
- Investments.
- Calendar.
- Tasks.
- Email.
- Documents.
- Memory.
- Habits.
- Goals.
- Notifications.
- Settings.

The AI assistant should be accessible from the main application interface.

Do not compromise usability to fit every feature onto one screen.

---

# 9. AUTHENTICATION AND SECURITY

Implement secure user authentication.

Requirements:

- Registration.
- Login.
- Logout.
- Password hashing.
- Secure session management.
- Password reset where supported.
- Protected API routes.
- User-specific data isolation.
- Input validation.
- Rate limiting for sensitive endpoints.
- Secure file upload validation.
- Secure CORS configuration.
- Secrets management.
- Audit logging.

Use secure password hashing such as Argon2id.

Never store passwords in plaintext.

Never hardcode API keys.

Never commit `.env` files.

Create `.env.example` with placeholders only.

Use authorization checks at the backend level, not merely frontend route protection.

Every user must only access their own data.

---

# 10. DATABASE DESIGN

Design a normalized relational database.

Identify and implement the necessary entities, including:

- Users.
- Accounts.
- Transactions.
- Categories.
- Budgets.
- Policies.
- Bills.
- Subscriptions.
- Investments.
- Holdings.
- Watchlists.
- Calendar events.
- Tasks.
- Projects.
- Milestones.
- Email metadata.
- Documents.
- Document chunks.
- Memories.
- Habits.
- Habit logs.
- Goals.
- Notifications.
- Conversations.
- Messages.
- Agent execution records.
- Integration accounts.
- Audit events.

Use appropriate:

- Primary keys.
- Foreign keys.
- Unique constraints.
- Indexes.
- Timestamps.
- Soft deletion where justified.
- Database transactions.

Use Alembic migrations.

Never silently drop existing tables or erase existing user data.

---

# 11. API INTEGRATION MANAGEMENT

Create a centralized integration configuration system.

Every external integration must expose:

- Provider name.
- Configuration status.
- Connection status.
- Required credentials.
- Permissions.
- Last synchronization time.
- Last error.
- Disconnect functionality.

Separate integrations into:

1. Required for the selected AI configuration.
2. Required for optional external features.
3. Completely optional enhancements.

If credentials are unavailable:

- The application must still start.
- Unrelated modules must continue working.
- Show the integration as disconnected.
- Explain exactly what is missing.
- Provide setup instructions.
- Avoid fake success responses.

Implement mock providers only for testing and development. Clearly label mock data.

Create the following documentation:

- `.env.example`
- `docs/API_KEYS_AND_SERVICES.md`
- `docs/INTEGRATION_SETUP.md`

The API key document must identify every external credential, its purpose, where to obtain it, whether it is mandatory, its corresponding environment variable and the feature that depends on it.

---

# 12. ERROR HANDLING AND OBSERVABILITY

Implement:

- Centralized exception handling.
- Structured application logs.
- Request IDs.
- Integration error tracking.
- Background job failure tracking.
- Database error handling.
- AI provider error handling.
- Retry policies.
- Health checks.
- Readiness checks.
- Application status endpoint.

Never swallow exceptions silently.

Never display raw stack traces or secrets to users.

Provide actionable error messages.

---

# 13. TESTING REQUIREMENTS

Testing is mandatory.

### Backend

Implement:

- Unit tests.
- Service tests.
- API tests.
- Database tests.
- Authentication tests.
- Authorization tests.
- Integration tests.
- Agent/tool tests.
- Validation tests.

### Frontend

Implement:

- Component tests.
- Form validation tests.
- API interaction tests.
- Navigation tests.
- Important workflow tests.

### End-to-end

Test complete workflows.

Examples:

1. Register and log in.
2. Add an expense.
3. Verify dashboard calculations.
4. Create a budget.
5. Trigger an overspending alert.
6. Add an insurance policy.
7. Schedule a renewal reminder.
8. Create and complete a task.
9. Create and track a habit.
10. Create a goal and update progress.
11. Upload and index a document.
12. Ask a document question.
13. Retrieve a saved memory.
14. Use the AI assistant to retrieve finance data.
15. Connect and synchronize Google Calendar when credentials are configured.
16. Search and summarize Gmail messages when credentials are configured.

Tests must not require real external API keys unless specifically testing a real provider.

Mock external APIs in automated tests.

Run all available checks and fix failures.

Do not claim tests passed unless they actually passed.

---

# 14. DEVELOPMENT EXECUTION STRATEGY

Work in controlled phases.

### Phase 1 — Repository audit and foundation

- Audit repository.
- Verify application startup.
- Review configuration.
- Review database schema.
- Fix existing critical failures.
- Establish baseline tests.
- Document architecture.

### Phase 2 — Core infrastructure

- Database improvements.
- Authentication.
- User isolation.
- Configuration.
- Error handling.
- Logging.
- Integration abstraction.

### Phase 3 — Core productivity modules

- Dashboard.
- Tasks.
- Projects.
- Calendar.
- Habits.
- Goals.
- Notifications.

### Phase 4 — Financial modules

- Accounts.
- Transactions.
- Budgets.
- Bills.
- Insurance.
- Investments.

### Phase 5 — Documents and communication

- Document management.
- RAG.
- Gmail.
- Google Calendar synchronization.

### Phase 6 — AI infrastructure

- LLM abstraction.
- Memory.
- LangGraph supervisor.
- Specialist agents.
- Tool execution.
- Human approvals.
- Conversation persistence.

### Phase 7 — Unified experience

- Global search.
- AI-powered workflows.
- Dashboard intelligence.
- Cross-module operations.
- Proactive monitoring.

### Phase 8 — Final quality assurance

- Full frontend validation.
- Full backend validation.
- Database migration testing.
- Integration testing.
- Security review.
- Performance review.
- Documentation.
- Final Git verification.

Do not leave earlier phases broken while moving to later phases.

---

# 15. MANDATORY GIT AND TERMINAL WORKFLOW

I work on Windows using Git Bash.

The project uses:

- `uv` for Python.
- `npm` for frontend packages.
- Git for version control.

All terminal instructions must be compatible with Git Bash.

Use commands such as:

```bash
uv sync
uv add package-name
uv remove package-name
uv run python -m pytest -q
uv run ruff check .
uv run ruff format --check .
npm install
npm run dev
npm run build
npm run lint
```

Adapt commands to the actual repository scripts and directory structure.

For every implementation phase:

1. Explain the objective.
2. List files being created.
3. List files being modified.
4. Explain significant architectural decisions.
5. Provide exact Git Bash commands.
6. Run the commands where your execution environment permits.
7. Inspect the resulting Git diff.
8. Run relevant tests.
9. Report the results.
10. Commit completed work using a descriptive commit message when appropriate.

Do not assume a command succeeded because you printed it.

If you cannot execute a command, explicitly tell me.

### Git safety

- Inspect `git status` before making changes.
- Never discard uncommitted user changes.
- Never use `git reset --hard` as a cleanup shortcut.
- Never force-push.
- Never overwrite existing work without inspection.
- Keep generated files out of Git where appropriate.
- Ensure `.env`, secrets, database files and sensitive uploads are ignored.

At every milestone, provide:

```bash
git status --short
git diff --check
git diff --stat
```

---

# 16. DOCUMENTATION DELIVERABLES

Maintain the following documentation:

- `README.md`
- `docs/ARCHITECTURE.md`
- `docs/IMPLEMENTATION_AUDIT.md`
- `docs/IMPLEMENTATION_PROGRESS.md`
- `docs/API_KEYS_AND_SERVICES.md`
- `docs/INTEGRATION_SETUP.md`
- `docs/DATABASE_SCHEMA.md`
- `docs/API_DOCUMENTATION.md`
- `docs/TESTING.md`
- `docs/DEPLOYMENT.md`
- `.env.example`

Update documentation as implementation changes.

The README must explain:

- What LIFEOS does.
- Architecture.
- Prerequisites.
- Installation.
- Environment configuration.
- Database setup.
- Migration commands.
- Frontend startup.
- Backend startup.
- Testing.
- Integration setup.
- Troubleshooting.

---

# 17. FINAL ACCEPTANCE CRITERIA

LIFEOS is not complete until all of the following are true:

[ ] Existing repository audited and preserved.

[ ] Frontend starts successfully.

[ ] Backend starts successfully.

[ ] Database connects successfully.

[ ] Migrations run successfully.

[ ] Authentication works.

[ ] User data is isolated.

[ ] Dashboard uses actual database data.

[ ] Finance management works end to end.

[ ] Budgets and analytics work.

[ ] Insurance management works.

[ ] Bills and subscriptions work.

[ ] Investment portfolio management works.

[ ] Calendar works locally and supports real Google integration.

[ ] Task management works.

[ ] Project management works.

[ ] Gmail works when configured.

[ ] Document upload and processing work.

[ ] RAG retrieval works.

[ ] Persistent AI memory works.

[ ] Habit tracking works.

[ ] Goal management works.

[ ] Notifications work.

[ ] Background jobs execute reliably.

[ ] Multi-agent orchestration works.

[ ] Agents invoke real backend tools.

[ ] Unified search works.

[ ] AI actions enforce permissions and confirmation.

[ ] Frontend is responsive and polished.

[ ] Automated tests pass.

[ ] Security review is completed.

[ ] Environment documentation is complete.

[ ] API credentials checklist is complete.

[ ] Git working tree is understood and clean apart from intentional user changes.

A feature that requires an unavailable third-party credential may be marked **integration-pending**, but its local functionality, configuration handling and error states must work.

Do not mark the entire project complete while core modules are still placeholders.

---

# 18. HOW YOU MUST REPORT PROGRESS

Maintain `docs/IMPLEMENTATION_PROGRESS.md`.

For every module, record:

- Status: Not started / In progress / Implemented / Tested / Integration-pending.
- Backend implementation.
- Frontend implementation.
- Database implementation.
- Integration status.
- Test results.
- Remaining issues.

Give me exact commands to execute in Git Bash.

If an API key is required, tell me:

1. Which provider.
2. Why it is required.
3. Where to obtain it.
4. The exact environment variable.
5. Where to place it.
6. Whether a free alternative exists.
7. Whether the feature can operate without it.

Never ask me to paste secret API keys into the chat.

Use placeholders in configuration examples.

---

# 19. YOUR FIRST ACTION

Start by inspecting the existing LIFEOS repository.

Do not immediately generate a new application.

Do not replace the current frontend or backend.

Do not generate a huge unverified ZIP.

First establish the actual repository state, then implement the project incrementally, integrating and testing each module.

After the audit, start Phase 1 and continue through the implementation phases.

You are responsible for engineering the complete application, not just producing recommendations.

**FINAL DIRECTIVE: BUILD A WORKING LIFEOS, NOT A DEMONSTRATION OF WHAT LIFEOS COULD EVENTUALLY BECOME.**