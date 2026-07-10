export type Role = "user" | "assistant"

export type Message = {
  id: string
  role: Role
  content: string
  createdAt: number
}

export type Conversation = {
  id: string
  title: string
  messages: Message[]
  updatedAt: number
  /** Name of the active document/source this conversation is grounded on. */
  source?: string
}

export type Book = {
  id: string
  title: string
  author: string
  cover: string
  /** approximate size shown in the upload chip */
  pages: number
  accent: string
  filename: string
}

/**
 * Demo "RAG projects" — a small library the user can pick from.
 * Selecting one behaves as if that document was uploaded.
 */
export const BOOKS: Book[] = [
  {
    id: "data-science-scratch",
    title: "Data Science from Scratch",
    author: "Joel Grus",
    cover: "/books/data-science-cover.png",
    pages: 388,
    accent: "oklch(0.68 0.15 258)",
    filename: "Data_Science_From_Scratch.pdf",
  },
  {
   id: "medical book",
   title: "Medical Book",
   author: "JACQUELINE ",
   cover: "/books/medical_book.png",
   pages: 637,
   accent: "",
   filename: "Medical_book.pdf",
 },

]

export const MEDICAL_QUESTIONS: string[] = [
 "What is abdominal ultrasound, and how does it work?",
 "What are the causes and symptoms of liver disease according to the book?",
 "What is the difference between ultrasound and CT scan?",
 "What are the available treatments and possible risks for gallstones?",
 "Explain the complete abdominal ultrasound procedure step by step, including preparation, precautions, and aftercare.",
 "A patient has severe abdominal pain and the doctor suspects an abdominal aortic aneurysm. Why is ultrasound recommended in this case?",
]

export const DATA_SCIENCE_QUESTIONS: string[] = [
  "What is data science, and what three skills are at its core?",
  "Why does the author choose Python for this book instead of R or Java?",
  "Explain how the friends_of_friend_ids() function works in the DataSciencester example.",
  "Why is degree centrality not always a good measure of importance in a social network?",
  "According to the salary analysis example, how does experience affect a data scientist's salary?",
  "What is the difference between a list, tuple, and dictionary in Python? Give examples from the book.",
]

export function getSuggestedQuestions(activeSource?: string): string[] {
  if (activeSource === "Data_Science_From_Scratch.pdf") {
    return DATA_SCIENCE_QUESTIONS
  }
  if (activeSource === "Medical_book.pdf") {
    return MEDICAL_QUESTIONS
  }
  return []
}



export function createId() {
  return Math.random().toString(36).slice(2) + Date.now().toString(36)
}

/**
 * Placeholder answer generator. Replace this with a real RAG pipeline
 * (retrieval + LLM) when you wire up your backend.
 */
export function mockAnswer(question: string, source?: string): string {
  const grounding = source
    ? `Based on **${source}**, here is what I found:`
    : "Here's a general response (no document selected yet):"

  return [
    grounding,
    "",
    `You asked: "${question.trim()}"`,
    "",
    "This is a placeholder answer so you can see how grounded responses will render. Wire this component up to your retrieval-augmented generation backend to return real, citation-backed answers pulled directly from the selected source.",
    "",
    "• Retrieved relevant passages from the source\n• Ranked them by semantic similarity\n• Composed an answer using only that context",
  ].join("\n")
}
