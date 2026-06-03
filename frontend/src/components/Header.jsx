export default function Header() {
  return (
    <header className="fixed top-0 left-0 right-0 z-50 pt-6 pb-4">
      <div className="max-w-7xl mx-auto px-6 flex justify-center items-center">
        <div className="relative inline-block">
          <span className="text-3xl md:text-4xl font-black tracking-tighter text-foreground uppercase relative z-10 box-sketch-no-hover px-6 py-2 bg-paper rotate-1 inline-block">
            AI Coding Tutor
          </span>
          {/* Hand-drawn marker splash */}
          <div className="absolute -z-10 bg-accent top-2 -left-2 w-[105%] h-[80%] rounded-[2px_15px_3px_15px] opacity-60 -rotate-2"></div>
        </div>
      </div>
    </header>
  );
}
