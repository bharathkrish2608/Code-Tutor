import ReactMarkdown from "react-markdown";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { vscDarkPlus } from "react-syntax-highlighter/dist/esm/styles/prism";

export default function FeedbackDisplay({ result }) {
  if (!result) {
    return (
      <div className="box-sketch h-full min-h-[500px] flex flex-col items-center justify-center p-12 text-center relative notebook-lines">
        <div className="absolute top-10 right-10">
          <svg
            className="w-16 h-16 text-primary/40 -rotate-12"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            viewBox="0 0 100 100"
          >
            <path d="M50 20 Q80 40 50 80 Q20 40 50 20 Z" />
          </svg>
        </div>

        <div className="relative mb-6">
          <svg
            className="w-16 h-16 text-foreground"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            viewBox="0 0 24 24"
          >
            <path d="M12 20h9M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z" />
          </svg>
          <div className="absolute -bottom-2 -right-4 font-handwritten text-secondary text-2xl rotate-[-10deg]">
            waiting...
          </div>
        </div>
        <h3 className="text-2xl font-black text-foreground mb-3 relative inline-block">
          AI Notes Area
          <svg
            className="absolute w-full h-2 bottom-0 left-0 text-accent -z-10"
            preserveAspectRatio="none"
            viewBox="0 0 100 10"
          >
            <path
              d="M0,5 Q50,15 100,5"
              stroke="currentColor"
              strokeWidth="6"
              fill="none"
            />
          </svg>
        </h3>
        <p className="text-muted-foreground font-handwritten text-2xl max-w-xs mt-2 leading-relaxed">
          Paste your script and hit analyze. I'll take a look!
        </p>
      </div>
    );
  }

  return (
    <div className="box-sketch h-full flex flex-col overflow-hidden relative">
      <div className="px-6 py-4 bg-paper/90 border-b-2 border-foreground/10 flex items-center justify-between sticky top-0 z-20 backdrop-blur-sm">
        <div className="flex items-center gap-3">
          <svg
            className="w-6 h-6 text-primary"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            viewBox="0 0 24 24"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7" />
            <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z" />
          </svg>
          <h2 className="text-sm font-bold uppercase tracking-widest text-foreground font-sans">
            Notes & Corrections
          </h2>
        </div>
        <span className="font-handwritten text-secondary font-bold text-xl rotate-[-2deg]">
          Reviewed!
        </span>
      </div>

      <div className="p-8 overflow-y-auto flex-grow prose prose-slate max-w-none notebook-lines text-foreground">
        <ReactMarkdown
          components={{
            code({ node, inline, className, children, ...props }) {
              const match = /language-(\w+)/.exec(className || "");
              return !inline && match ? (
                <div className="relative my-10 group">
                  <div className="absolute -top-6 -left-4 font-handwritten text-2xl text-primary rotate-[-5deg] z-10 flex items-center">
                    Fixed version!
                    <svg
                      className="w-6 h-6 ml-1 translate-y-2 opacity-80"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth="2"
                        d="M19 14l-7 7m0 0l-7-7m7 7V3"
                      ></path>
                    </svg>
                  </div>
                  <div className="box-sketch-no-hover overflow-hidden shadow-lg border-2 border-foreground bg-[#1e1e1e]">
                    <div className="bg-foreground px-4 py-2 text-[10px] text-paper font-bold uppercase tracking-widest flex justify-between border-b-2 border-foreground">
                      <span>{match[1]}</span>
                    </div>
                    <SyntaxHighlighter
                      style={vscDarkPlus}
                      language={match[1]}
                      PreTag="div"
                      customStyle={{
                        margin: 0,
                        padding: "1.5rem",
                        background: "#1e1e1e",
                        fontSize: "0.85rem",
                      }}
                      {...props}
                    >
                      {String(children).replace(/\n$/, "")}
                    </SyntaxHighlighter>
                  </div>
                </div>
              ) : (
                <code
                  className="bg-accent/40 text-foreground px-1.5 py-0.5 rounded font-mono text-[0.85em] border border-accent"
                  {...props}
                >
                  {children}
                </code>
              );
            },
            h1: ({ node, ...props }) => (
              <h1
                className="text-3xl font-black mt-8 first:mt-0 mb-6 text-foreground font-sans relative inline-block"
                {...props}
              />
            ),
            h2: ({ node, ...props }) => (
              <div className="relative mt-12 mb-6">
                <h2 className="text-xl inline-block font-bold text-foreground relative z-10 font-sans pl-2">
                  {props.children}
                </h2>
                <svg
                  className="absolute -left-2 top-1 w-[calc(100%+16px)] h-[120%] text-accent z-0 -rotate-1"
                  preserveAspectRatio="none"
                  viewBox="0 0 100 100"
                >
                  <path
                    d="M0,50 Q40,30 100,50 Q60,70 0,50 Z"
                    fill="currentColor"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinejoin="round"
                  />
                </svg>
              </div>
            ),
            h3: ({ node, ...props }) => (
              <h3
                className="text-lg font-bold mt-8 mb-3 text-foreground font-sans flex items-center gap-2 before:content-['>'] before:font-handwritten before:text-primary before:text-2xl"
                {...props}
              />
            ),
            p: ({ node, ...props }) => (
              <p
                className="mb-5 text-foreground leading-relaxed text-[1rem] font-sans"
                {...props}
              />
            ),
            ul: ({ node, ...props }) => (
              <ul className="list-none mb-8 space-y-4 pl-2" {...props} />
            ),
            li: ({ node, ...props }) => (
              <li className="flex gap-3 text-foreground text-[1rem] font-sans relative">
                <span className="font-handwritten text-secondary text-xl mt-[-4px] select-none">
                  *
                </span>
                <span>{props.children}</span>
              </li>
            ),
            blockquote: ({ node, ...props }) => (
              <div className="relative my-8 group">
                <svg
                  className="absolute -left-8 top-2 w-6 h-6 text-primary font-bold -rotate-12"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="3"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    d="M14 5l7 7m0 0l-7 7m7-7H3"
                  />
                </svg>
                <blockquote
                  className="border-2 border-foreground border-dashed pl-6 py-4 bg-paper text-foreground italic shadow-[4px_4px_0px_rgba(0,0,0,0.1)] relative"
                  {...props}
                >
                  <span className="absolute -top-3 right-4 bg-paper px-2 font-handwritten text-primary text-xl font-bold rotate-6">
                    pay attention!
                  </span>
                  {props.children}
                </blockquote>
              </div>
            ),
            strong: ({ node, ...props }) => (
              <strong
                className="font-black text-foreground relative rough-highlight marker-orange inline-block px-1"
                {...props}
              />
            ),
          }}
        >
          {result}
        </ReactMarkdown>
      </div>
    </div>
  );
}
