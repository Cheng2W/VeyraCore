'use client';

import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [healthStatus, setHealthStatus] = useState<string>('Loading...');

  useEffect(() => {
    axios
      .get('/api/health')
      .then((res) => {
        setHealthStatus(`Status: ${res.data.status} | Service: ${res.data.service} | Version: ${res.data.version}`);
      })
      .catch((err) => {
        setHealthStatus(`Error: ${err.message}`);
      });
  }, []);

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div className="z-10 w-full max-w-5xl items-center justify-between font-mono text-sm lg:flex">
        <h1 className="text-4xl font-bold mb-8">VeyraCore / 灵枢</h1>
      </div>
      
      <div className="mt-8 p-6 bg-white rounded-lg shadow-lg">
        <h2 className="text-xl font-semibold mb-4">System Health</h2>
        <p className="text-gray-700">{healthStatus}</p>
      </div>

      <div className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-6 w-full max-w-4xl">
        <div className="p-4 border rounded-lg hover:shadow-md transition">
          <h3 className="font-semibold">Backend</h3>
          <p className="text-sm text-gray-500">FastAPI + SQLAlchemy</p>
        </div>
        <div className="p-4 border rounded-lg hover:shadow-md transition">
          <h3 className="font-semibold">Frontend</h3>
          <p className="text-sm text-gray-500">Next.js + TailwindCSS</p>
        </div>
        <div className="p-4 border rounded-lg hover:shadow-md transition">
          <h3 className="font-semibold">Services</h3>
          <p className="text-sm text-gray-500">PostgreSQL + Redis + Celery</p>
        </div>
      </div>
    </main>
  );
}
