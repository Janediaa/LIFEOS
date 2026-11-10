import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { useEffect } from 'react';
import { useAuthStore } from '@/stores/authStore';
import AppLayout from '@/layouts/AppLayout';
import LoginPage from '@/pages/LoginPage';
import RegisterPage from '@/pages/RegisterPage';
import DashboardPage from '@/pages/DashboardPage';
import PlaceholderPage from '@/pages/PlaceholderPage';

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 30_000,
      retry: 1,
    },
  },
});

function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const { isAuthenticated } = useAuthStore();
  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }
  return <>{children}</>;
}

function AuthRoute({ children }: { children: React.ReactNode }) {
  const { isAuthenticated } = useAuthStore();
  if (isAuthenticated) {
    return <Navigate to="/" replace />;
  }
  return <>{children}</>;
}

function AppInit({ children }: { children: React.ReactNode }) {
  const { loadUser, isAuthenticated } = useAuthStore();

  useEffect(() => {
    if (isAuthenticated) {
      loadUser();
    }
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  return <>{children}</>;
}

export default function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <AppInit>
          <Routes>
            {/* Public routes */}
            <Route path="/login" element={<AuthRoute><LoginPage /></AuthRoute>} />
            <Route path="/register" element={<AuthRoute><RegisterPage /></AuthRoute>} />

            {/* Protected routes */}
            <Route
              element={
                <ProtectedRoute>
                  <AppLayout />
                </ProtectedRoute>
              }
            >
              <Route index element={<DashboardPage />} />
              <Route path="assistant" element={<PlaceholderPage title="AI Assistant" description="Multi-agent conversational AI — coming in Phase 6." />} />
              <Route path="finance" element={<PlaceholderPage title="Finance" description="Personal finance management — coming in Phase 4." />} />
              <Route path="insurance" element={<PlaceholderPage title="Insurance" description="Insurance and policy management — coming in Phase 4." />} />
              <Route path="bills" element={<PlaceholderPage title="Bills & Subscriptions" description="Recurring payment tracking — coming in Phase 4." />} />
              <Route path="investments" element={<PlaceholderPage title="Investments" description="Portfolio management and research — coming in Phase 4." />} />
              <Route path="calendar" element={<PlaceholderPage title="Calendar" description="Calendar and scheduling — coming in Phase 3." />} />
              <Route path="tasks" element={<PlaceholderPage title="Tasks & Projects" description="Task and project management — coming in Phase 3." />} />
              <Route path="email" element={<PlaceholderPage title="Email" description="Gmail intelligence — coming in Phase 5." />} />
              <Route path="documents" element={<PlaceholderPage title="Documents" description="Document management and RAG — coming in Phase 5." />} />
              <Route path="memory" element={<PlaceholderPage title="Memory" description="Persistent AI memory — coming in Phase 6." />} />
              <Route path="habits" element={<PlaceholderPage title="Habits" description="Habit tracking — coming in Phase 3." />} />
              <Route path="goals" element={<PlaceholderPage title="Goals" description="Goal management — coming in Phase 3." />} />
              <Route path="notifications" element={<PlaceholderPage title="Notifications" description="Notification center — coming in Phase 3." />} />
              <Route path="settings" element={<PlaceholderPage title="Settings" description="Application settings — coming in Phase 2." />} />
            </Route>

            {/* 404 */}
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </AppInit>
      </BrowserRouter>
    </QueryClientProvider>
  );
}
