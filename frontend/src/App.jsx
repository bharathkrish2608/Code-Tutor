import { useState, useEffect } from "react";
import Header from "./components/Header";
import CodeEditor from "./components/CodeEditor";
import FeedbackDisplay from "./components/FeedbackDisplay";
import { analyzeCode } from "./services/api";

function App() {
  const [code, setCode] = useState("");
  const [result, setResult] = useState("");
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [apiError, setApiError] = useState("");

  useEffect(() => {
    // Silent warm-up ping to wake up Render server immediately when user lands on page
    const API_URL = import.meta.env.VITE_API_URL || 'https://code-tutor-m4di.onrender.com/api';
    fetch(`${API_URL}/analyze/`, { method: 'OPTIONS' }).catch(() => {});
  }, []);


  const handleAnalyze = async () => {
    if (!code.trim()) {
      setApiError("Please enter some code to analyze.");
      return;
    }

    setIsAnalyzing(true);
    setApiError("");
    setResult("");

    try {
      const analysisResult = await analyzeCode(code);
      setResult(analysisResult);
    } catch (error) {
      setApiError(error.message || "An unexpected error occurred.");
      console.error(error);
    } finally {
      setIsAnalyzing(false);
    }
  };

  return (
    <div className="relative min-h-screen font-sans bg-paper text-foreground selection:bg-accent selection:text-foreground">
      {/* Subtle paper texture overlay (optional, achieved through CSS noise or just solid off-white) */}

      <Header />

      <main className="relative pt-36 pb-12 px-6 max-w-[1400px] mx-auto min-h-screen flex flex-col">
        <div className="text-center mb-10 relative">
          <h2 className="text-3xl md:text-5xl font-black text-foreground tracking-tight mb-4 relative inline-block">
            Master Code with{" "}
            <span className="relative inline-block px-2">
              <span className="relative z-10">AI Intelligence</span>
              {/* Rough hand-drawn highlight behind text */}
              <svg
                className="absolute inset-0 w-full h-[120%] -bottom-1 z-0 text-accent opacity-80"
                viewBox="0 0 100 100"
                preserveAspectRatio="none"
              >
                <path
                  d="M5,50 Q40,30 95,45 Q90,65 10,75 Q20,95 90,80"
                  stroke="currentColor"
                  strokeWidth="20"
                  strokeLinecap="round"
                  fill="none"
                  opacity="0.6"
                />
                <path
                  d="M5,50 Q40,30 95,45 Q90,65 10,75 Q20,95 90,80"
                  fill="currentColor"
                  opacity="0.8"
                />
              </svg>
            </span>
          </h2>
          <p className="text-base text-muted-foreground max-w-xl mx-auto leading-relaxed relative">
            Upload your Python scripts and get expert feedback in seconds.
            Simple, clean, and built for builders.
            {/* Small scribble arrow */}
            <svg
              className="absolute -right-8 top-[-20px] w-12 h-12 text-primary/80 -rotate-12"
              viewBox="0 0 100 100"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M20,80 Q40,60 80,30"
                stroke="currentColor"
                strokeWidth="4"
                strokeLinecap="round"
              />
              <path
                d="M80,30 L65,25 M80,30 L75,45"
                stroke="currentColor"
                strokeWidth="4"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
            <span className="absolute -right-24 top-[-25px] font-handwritten text-primary text-xl -rotate-12">
              try this!
            </span>
          </p>
        </div>

        <div className="flex flex-col xl:flex-row gap-10 xl:gap-14 min-h-[600px] mb-12 relative z-10 w-full">
          <div className="flex-1 min-w-0 h-full w-full">
            <CodeEditor
              code={code}
              setCode={setCode}
              onAnalyze={handleAnalyze}
              isAnalyzing={isAnalyzing}
              apiError={apiError}
            />
          </div>

          <div className="flex-[1.2] min-w-0 h-full w-full">
            <FeedbackDisplay result={result} />
          </div>
        </div>
      </main>

      <footer className="py-12 border-t-2 border-dashed border-border/80 mt-12 bg-white/50">
        <div className="max-w-7xl mx-auto px-6 text-center">
          <p className="font-bold text-foreground tracking-tight text-xl uppercase relative inline-block">
            AI Coding Tutor
            <svg
              className="absolute -bottom-2 left-0 w-full h-2 text-primary"
              viewBox="0 0 100 10"
              preserveAspectRatio="none"
            >
              <path
                d="M0,5 Q50,0 100,5 Q50,10 0,5"
                stroke="currentColor"
                strokeWidth="2"
                fill="none"
              />
            </svg>
          </p>
          <div className="mt-4 text-muted-foreground font-medium flex items-center justify-center gap-2">
            <span>Designed and developed by</span>
            <span className="font-handwritten text-foreground text-2xl rotate-[-2deg]">
              Bharath Krish
            </span>
          </div>
          <p className="text-muted-foreground/60 text-sm mt-3 mt-4">
            © 2026 All rights reserved
          </p>
        </div>
      </footer>
    </div>
  );
}

export default App;
