import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'VeyraCore - AI Service Platform',
  description: '灵枢/VeyraCore - AI Service Orchestration Platform',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
