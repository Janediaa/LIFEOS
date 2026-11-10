import { useAuthStore } from '@/stores/authStore';

export default function DashboardPage() {
  const { user } = useAuthStore();

  return (
    <div className="space-y-6">
      {/* Page header */}
      <div>
        <h1 className="text-2xl font-bold text-slate-900 dark:text-white">
          Welcome back{user?.full_name ? `, ${user.full_name}` : ''}
        </h1>
        <p className="text-slate-500 dark:text-slate-400 mt-1">
          Here's your personal overview for today.
        </p>
      </div>

      {/* Widget grid — empty states for now */}
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-4">
        <EmptyWidget title="Financial Balance" description="Add accounts and transactions to see your balance." />
        <EmptyWidget title="Monthly Expenses" description="Track your spending to see monthly expenses." />
        <EmptyWidget title="Savings Rate" description="Set up income and expenses to calculate your savings rate." />
        <EmptyWidget title="Budget Progress" description="Create budgets to track your spending progress." />
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
        <EmptyWidget title="Upcoming Bills" description="Add bills and subscriptions to see upcoming payments." tall />
        <EmptyWidget title="Calendar Events" description="Connect your calendar to see upcoming events." tall />
        <EmptyWidget title="Pending Tasks" description="Create tasks to see what's due." tall />
        <EmptyWidget title="Habit Tracker" description="Set up habits to track your daily progress." tall />
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-4">
        <EmptyWidget title="Active Goals" description="Create goals to track your progress." />
        <EmptyWidget title="Portfolio Summary" description="Add investments to see your portfolio overview." />
        <EmptyWidget title="AI Briefing" description="Configure an AI provider to receive daily briefings." />
      </div>
    </div>
  );
}

function EmptyWidget({ title, description, tall }: { title: string; description: string; tall?: boolean }) {
  return (
    <div
      className={`bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 p-5 ${
        tall ? 'min-h-[200px]' : 'min-h-[120px]'
      } flex flex-col`}
    >
      <h3 className="text-sm font-semibold text-slate-700 dark:text-slate-300 mb-2">{title}</h3>
      <div className="flex-1 flex items-center justify-center">
        <p className="text-sm text-slate-400 dark:text-slate-500 text-center">{description}</p>
      </div>
    </div>
  );
}

