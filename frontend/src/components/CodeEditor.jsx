export default function CodeEditor({
  code,
  setCode,
  onAnalyze,
  isAnalyzing,
  apiError,
}) {
  return (
    <div className="box-sketch h-full flex flex-col overflow-hidden group">
      <div className="px-6 py-4 flex justify-between items-center border-b-2 border-foreground/10 bg-white/50">
        <div className="flex items-center gap-3">
          <span className="font-bold uppercase tracking-widest text-foreground flex items-center gap-2">
            <svg
              className="w-4 h-4 text-primary"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"
              />
            </svg>
            Editor
          </span>
        </div>
        {code && (
          <button
            onClick={() => setCode("")}
            className="text-xs font-handwritten text-destructive text-xl hover:scale-110 transition-transform tracking-wider"
          >
            erase all (x)
          </button>
        )}
      </div>

      <div className="px-6 pb-6 flex-grow flex flex-col space-y-4 pt-4">
        {apiError && (
          <div className="box-sketch-no-hover bg-destructive/10 text-destructive p-4 text-sm flex items-center gap-3 border-destructive">
            <span className="font-handwritten text-xl font-bold">Oops!</span>
            {apiError}
          </div>
        )}

        <div className="relative flex-grow min-h-[300px]">
          <textarea
            value={code}
            onChange={(e) => setCode(e.target.value)}
            placeholder="# Paste your messy code here..."
            className="absolute inset-0 w-full h-full p-4 font-mono text-[15px] bg-transparent border-2 border-dashed border-border/80 rounded-xl focus:border-primary focus:ring-0 resize-none transition-colors scroll-smooth leading-relaxed text-foreground"
            spellCheck="false"
          />
        </div>

        <div className="pt-2 flex items-center justify-between relative">
          <p className="font-handwritten text-muted-foreground text-xl hidden sm:block -rotate-2">
            ready when you are...
          </p>
          <button
            onClick={onAnalyze}
            disabled={isAnalyzing || !code.trim()}
            className="relative px-8 py-3 text-foreground font-bold text-lg hover:bg-foreground/5 disabled:opacity-50 disabled:cursor-not-allowed transition-all box-sketch-no-hover !rounded-md overflow-visible group ml-auto"
          >
            <div className="relative z-10 flex items-center gap-2">
              {isAnalyzing ? (
                <>
                  <span className="font-handwritten text-2xl animate-pulse">
                    Thinking...
                  </span>
                </>
              ) : (
                <>
                  <span className="font-handwritten text-2xl">
                    Analyze Code
                  </span>
                </>
              )}
            </div>
            {/* Hand drawn arrow pointing to button */}
            {!isAnalyzing && code.trim() && (
              <svg
                className="absolute -left-12 top-1 w-10 h-10 text-primary opacity-0 group-hover:opacity-100 transition-opacity -rotate-12"
                viewBox="0 0 100 100"
                fill="none"
                stroke="currentColor"
                strokeWidth="4"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <path d="M10,50 Q40,40 80,50" />
                <path d="M70,40 L85,50 L70,60" />
              </svg>
            )}
          </button>
        </div>
      </div>
    </div>
  );
}
