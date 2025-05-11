import { Html, Head, Main, NextScript } from 'next/document';

// Custom HTML structure for SEO and accessibility
export default function Document() {
  return (
    <Html lang="en">
      <Head>
        <meta charSet="UTF-8" />
        <meta name="description" content="Legal Emotion Analyzer - Voice to Emotion AI for Family Law" />
        <link rel="icon" href="/favicon.ico" />
        <title>Legal Emotion Analyzer</title>
      </Head>
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  );
}
