export default function Header() {
  return (
    <header className="p-4 border-b">
      <nav className="flex justify-between items-center">
        <div className="font-bold text-xl">VeyraCore</div>
        <div className="space-x-4">
          <a href="/" className="hover:text-blue-500">Home</a>
          <a href="/dashboard" className="hover:text-blue-500">Dashboard</a>
          <a href="/settings" className="hover:text-blue-500">Settings</a>
        </div>
      </nav>
    </header>
  );
}
