---
name: code-standards

triggers:
  - "writing code"
  - "reviewing code"
  - "Next.js"
  - "React"
  - "TypeScript"
related:
  - "[[ui-ux-design]]"
  - "[[client-delivery]]"
  - "[[landing-page-generator]]"
description: >
  Code standards and conventions for Next.js, React, TypeScript, and Tailwind CSS projects.
  Use when: writing, reviewing, or scaffolding code in our stack.
  Don't use when: writing non-web code (shell scripts, Python, etc.), or for design-only decisions (use ui-ux-design instead).
  Output: Code that follows our conventions — consistent, typed, accessible, performant.
---

# Code Standards

**Stack:** Next.js (App Router), React (functional components, hooks), Tailwind CSS, TypeScript, Node.js

**Deploy:** Vercel or static export

---

## Table of Contents

1. [Next.js App Router Folder Structure](#nextjs-app-router-folder-structure)
2. [Server vs Client Components](#server-vs-client-components)
3. [TypeScript Conventions](#typescript-conventions)
4. [Tailwind CSS Conventions](#tailwind-css-conventions)
5. [Component Composition Patterns](#component-composition-patterns)
6. [State Management Patterns](#state-management-patterns)
7. [API Route Patterns](#api-route-patterns)
8. [Error Handling](#error-handling)
9. [Performance Optimization](#performance-optimization)
10. [Git Conventions](#git-conventions)
11. [File Naming & Import Ordering](#file-naming--import-ordering)
12. [Environment Variables](#environment-variables)
13. [Accessibility](#accessibility)
14. [Security Basics](#security-basics)

---

## Next.js App Router Folder Structure

### Standard Project Layout

```
project-root/
├── app/                      # App Router pages and layouts
│   ├── (auth)/              # Route groups (not in URL)
│   │   ├── login/
│   │   └── register/
│   ├── (marketing)/
│   │   ├── about/
│   │   └── pricing/
│   ├── api/                 # API routes
│   │   └── users/
│   │       └── route.ts
│   ├── dashboard/
│   │   ├── page.tsx         # /dashboard route
│   │   ├── layout.tsx       # Layout for dashboard
│   │   └── loading.tsx      # Loading UI
│   ├── layout.tsx           # Root layout
│   ├── page.tsx             # Home page (/)
│   ├── error.tsx            # Error boundary
│   └── not-found.tsx        # 404 page
├── components/              # Shared components
│   ├── ui/                  # Base UI components
│   │   ├── button.tsx
│   │   ├── input.tsx
│   │   └── card.tsx
│   ├── forms/               # Form components
│   └── layout/              # Layout components
│       ├── header.tsx
│       └── footer.tsx
├── lib/                     # Utility functions
│   ├── utils.ts
│   ├── api.ts
│   └── validations.ts
├── hooks/                   # Custom React hooks
│   ├── use-media-query.ts
│   └── use-local-storage.ts
├── types/                   # TypeScript type definitions
│   ├── index.ts
│   ├── user.ts
│   └── api.ts
├── styles/                  # Global styles
│   └── globals.css
├── public/                  # Static assets
│   ├── images/
│   └── fonts/
├── config/                  # Configuration files
│   ├── site.ts
│   └── constants.ts
└── middleware.ts            # Middleware (root level)
```

### Rules

- **Route groups** `(name)` organize routes without affecting URLs
- **Colocation**: Keep related components close to where they're used
- **Special files**: `page.tsx`, `layout.tsx`, `loading.tsx`, `error.tsx`, `not-found.tsx`
- **Private folders**: Prefix with `_` to exclude from routing (e.g., `_components`)
- **Parallel routes**: Use `@folder` for parallel route segments
- **Intercepting routes**: Use `(.)folder` for modal-style intercepts

---

## Server vs Client Components

### Default: Server Components

By default, all components in `app/` are **Server Components**. Use them unless you need interactivity.

### When to Use Server Components

✅ **Server Components** (default):
- Fetching data
- Accessing backend resources directly
- Keeping sensitive information on server (API keys, tokens)
- Large dependencies that don't need client-side JS
- Static content

```tsx
// app/posts/page.tsx
// ✅ Server Component (default)
import { db } from '@/lib/db'

export default async function PostsPage() {
  // Direct database access
  const posts = await db.post.findMany()
  
  return (
    <div>
      {posts.map(post => (
        <article key={post.id}>
          <h2>{post.title}</h2>
          <p>{post.excerpt}</p>
        </article>
      ))}
    </div>
  )
}
```

### When to Use Client Components

✅ **Client Components** (add `"use client"`):
- Event listeners (`onClick`, `onChange`, etc.)
- State hooks (`useState`, `useReducer`)
- Effect hooks (`useEffect`, `useLayoutEffect`)
- Browser-only APIs (`localStorage`, `window`, `document`)
- Custom hooks that use client-only features
- Class components (legacy)

```tsx
// components/search-input.tsx
'use client'

import { useState } from 'react'

export function SearchInput() {
  const [query, setQuery] = useState('')
  
  return (
    <input
      type="text"
      value={query}
      onChange={(e) => setQuery(e.target.value)}
      placeholder="Search..."
    />
  )
}
```

### Composition Pattern: Server + Client

Push `"use client"` as deep as possible. Wrap interactive parts only.

```tsx
// app/posts/page.tsx
// ✅ Server Component
import { SearchInput } from '@/components/search-input'
import { db } from '@/lib/db'

export default async function PostsPage() {
  const posts = await db.post.findMany()
  
  return (
    <div>
      {/* Client component for interactivity */}
      <SearchInput />
      
      {/* Server-rendered static content */}
      <div className="grid gap-4">
        {posts.map(post => (
          <article key={post.id}>
            <h2>{post.title}</h2>
          </article>
        ))}
      </div>
    </div>
  )
}
```

### Passing Server Data to Client Components

❌ **Don't** pass non-serializable data (functions, dates, class instances):

```tsx
// ❌ BAD
<ClientComponent 
  date={new Date()} 
  onClick={() => {}} 
/>
```

✅ **Do** serialize data:

```tsx
// ✅ GOOD
<ClientComponent 
  date={post.createdAt.toISOString()} 
  userId={user.id}
/>
```

---

## TypeScript Conventions

### Strict Mode

Always use strict mode in `tsconfig.json`:

```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true
  }
}
```

### Type vs Interface

**Rule:** Use `type` by default. Use `interface` only for object shapes that need extension.

```tsx
// ✅ Type for primitives, unions, tuples
type Status = 'pending' | 'active' | 'archived'
type Point = [number, number]
type ID = string | number

// ✅ Type for object shapes (most cases)
type User = {
  id: string
  name: string
  email: string
}

// ✅ Interface when you need declaration merging or extending
interface ApiResponse {
  status: number
  data: unknown
}

interface UserResponse extends ApiResponse {
  data: User
}
```

### Naming Conventions

```tsx
// Types: PascalCase
type UserRole = 'admin' | 'user'
type ApiResponse = { ... }

// Interfaces: PascalCase, optionally prefix with 'I' for clarity
interface ButtonProps { ... }
interface IApiClient { ... }  // if you prefer

// Type predicates: is*, has*
function isUser(value: unknown): value is User { ... }

// Generic type parameters: T, K, V or descriptive TData, TError
type Result<TData, TError = Error> = { ... }

// Const assertions for literal types
const ROUTES = {
  HOME: '/',
  DASHBOARD: '/dashboard'
} as const

// Enums: PascalCase (prefer union types instead)
// ❌ Avoid enums (runtime overhead)
enum Status { Active, Inactive }

// ✅ Use union types
type Status = 'active' | 'inactive'
```

### Component Props

```tsx
// ✅ Type the props explicitly
type ButtonProps = {
  variant?: 'primary' | 'secondary' | 'ghost'
  size?: 'sm' | 'md' | 'lg'
  disabled?: boolean
  children: React.ReactNode
  onClick?: () => void
}

export function Button({ 
  variant = 'primary', 
  size = 'md',
  disabled = false,
  children,
  onClick 
}: ButtonProps) {
  return <button onClick={onClick}>{children}</button>
}

// ✅ Extend HTML element props
import { ComponentPropsWithoutRef } from 'react'

type InputProps = ComponentPropsWithoutRef<'input'> & {
  label: string
  error?: string
}

export function Input({ label, error, ...props }: InputProps) {
  return (
    <div>
      <label>{label}</label>
      <input {...props} />
      {error && <span>{error}</span>}
    </div>
  )
}
```

### Utility Types

```tsx
// Extract keys of specific type
type KeysOfType<T, U> = {
  [K in keyof T]: T[K] extends U ? K : never
}[keyof T]

// Make specific fields required
type RequireFields<T, K extends keyof T> = T & Required<Pick<T, K>>

// Common utility types
type Partial<T>       // All properties optional
type Required<T>      // All properties required
type Pick<T, K>       // Select specific properties
type Omit<T, K>       // Exclude specific properties
type Record<K, T>     // Object with keys K and values T
type Exclude<T, U>    // Remove types from union
type Extract<T, U>    // Extract types from union
type NonNullable<T>   // Remove null/undefined
type ReturnType<T>    // Extract function return type
type Parameters<T>    // Extract function parameters

// Example usage
type User = {
  id: string
  name: string
  email: string
  role: 'admin' | 'user'
}

type UserPreview = Pick<User, 'id' | 'name'>
type UserUpdate = Partial<Omit<User, 'id'>>
type UserRoles = User['role'] // 'admin' | 'user'
```

### Async/Await Typing

```tsx
// ✅ Type async functions explicitly
async function fetchUser(id: string): Promise<User> {
  const response = await fetch(`/api/users/${id}`)
  return response.json()
}

// ✅ Type error handling
type Result<T, E = Error> = 
  | { success: true; data: T }
  | { success: false; error: E }

async function safeAsync<T>(
  fn: () => Promise<T>
): Promise<Result<T>> {
  try {
    const data = await fn()
    return { success: true, data }
  } catch (error) {
    return { 
      success: false, 
      error: error instanceof Error ? error : new Error('Unknown error')
    }
  }
}
```

---

## Tailwind CSS Conventions

### Configuration

```js
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class', // or 'media'
  content: [
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        // Custom color palette
        primary: {
          50: '#f0f9ff',
          100: '#e0f2fe',
          500: '#0ea5e9',
          600: '#0284c7',
          900: '#0c4a6e',
        },
        // Semantic colors
        brand: 'var(--color-brand)',
        accent: 'var(--color-accent)',
      },
      fontFamily: {
        sans: ['var(--font-inter)', 'system-ui', 'sans-serif'],
        mono: ['var(--font-mono)', 'monospace'],
      },
      spacing: {
        18: '4.5rem',
        88: '22rem',
      },
      animation: {
        'fade-in': 'fadeIn 0.2s ease-in',
        'slide-up': 'slideUp 0.3s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
}
```

### CSS Variables for Theme

```css
/* styles/globals.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --color-brand: 220 90% 56%;
    --color-accent: 280 80% 60%;
    --background: 0 0% 100%;
    --foreground: 240 10% 4%;
  }

  .dark {
    --background: 240 10% 4%;
    --foreground: 0 0% 98%;
  }
  
  body {
    @apply bg-background text-foreground;
  }
}
```

### Class Naming Patterns

```tsx
// ✅ Group by type: layout → spacing → colors → typography → effects
<div className="
  flex items-center justify-between
  px-4 py-2 gap-2
  bg-white dark:bg-gray-900
  text-sm font-medium
  rounded-lg shadow-sm
  hover:shadow-md transition-shadow
">

// ✅ Use cn() utility for conditional classes
import { cn } from '@/lib/utils'

<button 
  className={cn(
    "px-4 py-2 rounded-lg font-medium transition-colors",
    variant === 'primary' && "bg-blue-600 text-white hover:bg-blue-700",
    variant === 'secondary' && "bg-gray-200 text-gray-900 hover:bg-gray-300",
    disabled && "opacity-50 cursor-not-allowed"
  )}
/>

// lib/utils.ts
import { clsx, type ClassValue } from 'clsx'
import { twMerge } from 'tailwind-merge'

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
```

### Responsive Design

Mobile-first approach. Use breakpoints in order: `sm:` → `md:` → `lg:` → `xl:` → `2xl:`

```tsx
<div className="
  grid grid-cols-1 
  sm:grid-cols-2 
  lg:grid-cols-3 
  xl:grid-cols-4
  gap-4 sm:gap-6
  px-4 sm:px-6 lg:px-8
">
```

### Dark Mode

```tsx
// Use dark: prefix
<div className="bg-white dark:bg-gray-900 text-gray-900 dark:text-white">

// Toggle dark mode (client component)
'use client'

import { useTheme } from 'next-themes'

export function ThemeToggle() {
  const { theme, setTheme } = useTheme()
  
  return (
    <button onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}>
      Toggle theme
    </button>
  )
}

// app/layout.tsx (setup)
import { ThemeProvider } from 'next-themes'

export default function RootLayout({ children }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body>
        <ThemeProvider attribute="class" defaultTheme="system">
          {children}
        </ThemeProvider>
      </body>
    </html>
  )
}
```

### Component Variants with CVA

```tsx
// Use class-variance-authority for variant management
import { cva, type VariantProps } from 'class-variance-authority'

const buttonVariants = cva(
  // base styles
  'inline-flex items-center justify-center rounded-lg font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 disabled:pointer-events-none disabled:opacity-50',
  {
    variants: {
      variant: {
        primary: 'bg-blue-600 text-white hover:bg-blue-700',
        secondary: 'bg-gray-200 text-gray-900 hover:bg-gray-300',
        ghost: 'hover:bg-gray-100 dark:hover:bg-gray-800',
        destructive: 'bg-red-600 text-white hover:bg-red-700',
      },
      size: {
        sm: 'h-8 px-3 text-sm',
        md: 'h-10 px-4 text-base',
        lg: 'h-12 px-6 text-lg',
      },
    },
    defaultVariants: {
      variant: 'primary',
      size: 'md',
    },
  }
)

type ButtonProps = VariantProps<typeof buttonVariants> & {
  children: React.ReactNode
  onClick?: () => void
}

export function Button({ variant, size, children, onClick }: ButtonProps) {
  return (
    <button 
      className={buttonVariants({ variant, size })}
      onClick={onClick}
    >
      {children}
    </button>
  )
}
```

---

## Component Composition Patterns

### Compound Components

Use for related components that share state.

```tsx
// components/tabs.tsx
'use client'

import { createContext, useContext, useState } from 'react'

type TabsContextType = {
  activeTab: string
  setActiveTab: (tab: string) => void
}

const TabsContext = createContext<TabsContextType | null>(null)

function useTabs() {
  const context = useContext(TabsContext)
  if (!context) throw new Error('useTabs must be used within Tabs')
  return context
}

export function Tabs({ 
  children, 
  defaultTab 
}: { 
  children: React.ReactNode
  defaultTab: string 
}) {
  const [activeTab, setActiveTab] = useState(defaultTab)
  
  return (
    <TabsContext.Provider value={{ activeTab, setActiveTab }}>
      <div className="w-full">{children}</div>
    </TabsContext.Provider>
  )
}

export function TabsList({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex gap-2 border-b border-gray-200">
      {children}
    </div>
  )
}

export function TabsTrigger({ 
  value, 
  children 
}: { 
  value: string
  children: React.ReactNode 
}) {
  const { activeTab, setActiveTab } = useTabs()
  const isActive = activeTab === value
  
  return (
    <button
      onClick={() => setActiveTab(value)}
      className={cn(
        "px-4 py-2 font-medium transition-colors",
        isActive 
          ? "border-b-2 border-blue-600 text-blue-600" 
          : "text-gray-600 hover:text-gray-900"
      )}
    >
      {children}
    </button>
  )
}

export function TabsContent({ 
  value, 
  children 
}: { 
  value: string
  children: React.ReactNode 
}) {
  const { activeTab } = useTabs()
  if (activeTab !== value) return null
  
  return <div className="py-4">{children}</div>
}

// Usage
<Tabs defaultTab="account">
  <TabsList>
    <TabsTrigger value="account">Account</TabsTrigger>
    <TabsTrigger value="settings">Settings</TabsTrigger>
  </TabsList>
  <TabsContent value="account">
    <p>Account content</p>
  </TabsContent>
  <TabsContent value="settings">
    <p>Settings content</p>
  </TabsContent>
</Tabs>
```

### Render Props Pattern

```tsx
type RenderPropComponentProps<T> = {
  data: T[]
  render: (item: T) => React.ReactNode
}

export function List<T extends { id: string }>({ 
  data, 
  render 
}: RenderPropComponentProps<T>) {
  return (
    <ul className="space-y-2">
      {data.map(item => (
        <li key={item.id}>{render(item)}</li>
      ))}
    </ul>
  )
}

// Usage
<List 
  data={users} 
  render={(user) => (
    <div>{user.name}</div>
  )} 
/>
```

### Higher-Order Components (HOC)

Use sparingly. Prefer hooks or composition.

```tsx
// Use only when you need to enhance multiple components
function withAuth<P extends object>(
  Component: React.ComponentType<P>
) {
  return function AuthComponent(props: P) {
    const session = useSession()
    
    if (!session) {
      return <div>Please log in</div>
    }
    
    return <Component {...props} />
  }
}

// Usage
const ProtectedPage = withAuth(DashboardPage)
```

### Custom Hooks for Logic Reuse

✅ **Preferred pattern** for reusable logic.

```tsx
// hooks/use-toggle.ts
export function useToggle(initialValue = false) {
  const [value, setValue] = useState(initialValue)
  
  const toggle = useCallback(() => setValue(v => !v), [])
  const setTrue = useCallback(() => setValue(true), [])
  const setFalse = useCallback(() => setValue(false), [])
  
  return { value, toggle, setTrue, setFalse }
}

// hooks/use-debounce.ts
export function useDebounce<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState(value)
  
  useEffect(() => {
    const handler = setTimeout(() => setDebouncedValue(value), delay)
    return () => clearTimeout(handler)
  }, [value, delay])
  
  return debouncedValue
}

// Usage
function SearchComponent() {
  const [query, setQuery] = useState('')
  const debouncedQuery = useDebounce(query, 500)
  
  useEffect(() => {
    // Fetch with debouncedQuery
  }, [debouncedQuery])
  
  return <input value={query} onChange={e => setQuery(e.target.value)} />
}
```

---

## State Management Patterns

### Local State (useState)

Use for component-specific state.

```tsx
'use client'

export function Counter() {
  const [count, setCount] = useState(0)
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  )
}
```

### Complex Local State (useReducer)

Use when state logic is complex or involves multiple sub-values.

```tsx
'use client'

type State = {
  loading: boolean
  error: string | null
  data: User | null
}

type Action =
  | { type: 'FETCH_START' }
  | { type: 'FETCH_SUCCESS'; payload: User }
  | { type: 'FETCH_ERROR'; payload: string }

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case 'FETCH_START':
      return { ...state, loading: true, error: null }
    case 'FETCH_SUCCESS':
      return { loading: false, error: null, data: action.payload }
    case 'FETCH_ERROR':
      return { loading: false, error: action.payload, data: null }
    default:
      return state
  }
}

export function UserProfile({ userId }: { userId: string }) {
  const [state, dispatch] = useReducer(reducer, {
    loading: false,
    error: null,
    data: null
  })
  
  useEffect(() => {
    dispatch({ type: 'FETCH_START' })
    
    fetch(`/api/users/${userId}`)
      .then(res => res.json())
      .then(data => dispatch({ type: 'FETCH_SUCCESS', payload: data }))
      .catch(err => dispatch({ type: 'FETCH_ERROR', payload: err.message }))
  }, [userId])
  
  if (state.loading) return <div>Loading...</div>
  if (state.error) return <div>Error: {state.error}</div>
  if (!state.data) return null
  
  return <div>{state.data.name}</div>
}
```

### Global State (Context)

Use Context for theme, auth, or app-wide settings. Not for frequently changing data.

```tsx
// lib/auth-context.tsx
'use client'

import { createContext, useContext, useState, useEffect } from 'react'

type AuthContextType = {
  user: User | null
  login: (email: string, password: string) => Promise<void>
  logout: () => Promise<void>
}

const AuthContext = createContext<AuthContextType | null>(null)

export function useAuth() {
  const context = useContext(AuthContext)
  if (!context) throw new Error('useAuth must be used within AuthProvider')
  return context
}

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null)
  
  useEffect(() => {
    // Check session on mount
    fetch('/api/auth/session')
      .then(res => res.json())
      .then(data => setUser(data.user))
  }, [])
  
  const login = async (email: string, password: string) => {
    const res = await fetch('/api/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password })
    })
    const data = await res.json()
    setUser(data.user)
  }
  
  const logout = async () => {
    await fetch('/api/auth/logout', { method: 'POST' })
    setUser(null)
  }
  
  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  )
}

// app/layout.tsx
export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        <AuthProvider>
          {children}
        </AuthProvider>
      </body>
    </html>
  )
}
```

### URL State (searchParams)

Use for shareable, bookmarkable state.

```tsx
// app/products/page.tsx
export default function ProductsPage({
  searchParams
}: {
  searchParams: { sort?: string; category?: string }
}) {
  const sort = searchParams.sort ?? 'newest'
  const category = searchParams.category
  
  return <ProductList sort={sort} category={category} />
}

// Client component for updating URL
'use client'

import { useRouter, useSearchParams } from 'next/navigation'

export function FilterControls() {
  const router = useRouter()
  const searchParams = useSearchParams()
  
  const updateFilter = (key: string, value: string) => {
    const params = new URLSearchParams(searchParams.toString())
    params.set(key, value)
    router.push(`?${params.toString()}`)
  }
  
  return (
    <select onChange={(e) => updateFilter('sort', e.target.value)}>
      <option value="newest">Newest</option>
      <option value="popular">Popular</option>
    </select>
  )
}
```

### External State Libraries

For complex apps, consider:
- **Zustand** (lightweight, simple API)
- **Jotai** (atomic state)
- **Redux Toolkit** (enterprise apps)

```tsx
// lib/store.ts (Zustand example)
import { create } from 'zustand'

type CartStore = {
  items: CartItem[]
  addItem: (item: CartItem) => void
  removeItem: (id: string) => void
  clearCart: () => void
}

export const useCartStore = create<CartStore>((set) => ({
  items: [],
  addItem: (item) => set((state) => ({ 
    items: [...state.items, item] 
  })),
  removeItem: (id) => set((state) => ({ 
    items: state.items.filter(item => item.id !== id) 
  })),
  clearCart: () => set({ items: [] }),
}))

// Usage
'use client'

export function Cart() {
  const { items, removeItem } = useCartStore()
  
  return (
    <div>
      {items.map(item => (
        <div key={item.id}>
          {item.name}
          <button onClick={() => removeItem(item.id)}>Remove</button>
        </div>
      ))}
    </div>
  )
}
```

---

## API Route Patterns

### Basic Structure

```ts
// app/api/users/route.ts
import { NextRequest, NextResponse } from 'next/server'

// GET /api/users
export async function GET(request: NextRequest) {
  try {
    const searchParams = request.nextUrl.searchParams
    const query = searchParams.get('query')
    
    const users = await db.user.findMany({
      where: query ? {
        name: { contains: query }
      } : undefined
    })
    
    return NextResponse.json({ users })
  } catch (error) {
    return NextResponse.json(
      { error: 'Failed to fetch users' },
      { status: 500 }
    )
  }
}

// POST /api/users
export async function POST(request: NextRequest) {
  try {
    const body = await request.json()
    
    // Validation
    const validated = userSchema.parse(body)
    
    const user = await db.user.create({
      data: validated
    })
    
    return NextResponse.json({ user }, { status: 201 })
  } catch (error) {
    if (error instanceof z.ZodError) {
      return NextResponse.json(
        { error: 'Invalid input', details: error.errors },
        { status: 400 }
      )
    }
    
    return NextResponse.json(
      { error: 'Failed to create user' },
      { status: 500 }
    )
  }
}
```

### Dynamic Routes

```ts
// app/api/users/[id]/route.ts
type Params = {
  params: {
    id: string
  }
}

export async function GET(
  request: NextRequest,
  { params }: Params
) {
  const user = await db.user.findUnique({
    where: { id: params.id }
  })
  
  if (!user) {
    return NextResponse.json(
      { error: 'User not found' },
      { status: 404 }
    )
  }
  
  return NextResponse.json({ user })
}

export async function PATCH(
  request: NextRequest,
  { params }: Params
) {
  const body = await request.json()
  
  const user = await db.user.update({
    where: { id: params.id },
    data: body
  })
  
  return NextResponse.json({ user })
}

export async function DELETE(
  request: NextRequest,
  { params }: Params
) {
  await db.user.delete({
    where: { id: params.id }
  })
  
  return NextResponse.json({ success: true }, { status: 204 })
}
```

### Middleware & Auth

```ts
// lib/auth.ts
import { NextRequest } from 'next/server'
import { verify } from 'jsonwebtoken'

export async function requireAuth(request: NextRequest) {
  const token = request.headers.get('authorization')?.split(' ')[1]
  
  if (!token) {
    throw new Error('Unauthorized')
  }
  
  try {
    const payload = verify(token, process.env.JWT_SECRET!)
    return payload as { userId: string }
  } catch {
    throw new Error('Invalid token')
  }
}

// app/api/protected/route.ts
export async function GET(request: NextRequest) {
  try {
    const { userId } = await requireAuth(request)
    
    const data = await db.user.findUnique({
      where: { id: userId }
    })
    
    return NextResponse.json({ data })
  } catch (error) {
    return NextResponse.json(
      { error: 'Unauthorized' },
      { status: 401 }
    )
  }
}
```

### Response Helpers

```ts
// lib/api-response.ts
export class ApiResponse {
  static success<T>(data: T, status = 200) {
    return NextResponse.json({ success: true, data }, { status })
  }
  
  static error(message: string, status = 500) {
    return NextResponse.json(
      { success: false, error: message },
      { status }
    )
  }
  
  static validationError(errors: Record<string, string>) {
    return NextResponse.json(
      { success: false, error: 'Validation failed', errors },
      { status: 400 }
    )
  }
  
  static notFound(resource = 'Resource') {
    return NextResponse.json(
      { success: false, error: `${resource} not found` },
      { status: 404 }
    )
  }
  
  static unauthorized(message = 'Unauthorized') {
    return NextResponse.json(
      { success: false, error: message },
      { status: 401 }
    )
  }
}

// Usage
export async function GET(request: NextRequest) {
  const user = await db.user.findUnique({ where: { id: '123' } })
  
  if (!user) {
    return ApiResponse.notFound('User')
  }
  
  return ApiResponse.success(user)
}
```

---

## Error Handling

### Client-Side Error Boundaries

```tsx
// app/error.tsx
'use client'

import { useEffect } from 'react'

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  useEffect(() => {
    // Log to error reporting service
    console.error('Error:', error)
  }, [error])

  return (
    <div className="flex min-h-screen items-center justify-center">
      <div className="text-center">
        <h2 className="text-2xl font-bold mb-4">Something went wrong!</h2>
        <p className="text-gray-600 mb-4">{error.message}</p>
        <button
          onClick={reset}
          className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
        >
          Try again
        </button>
      </div>
    </div>
  )
}

// app/not-found.tsx
export default function NotFound() {
  return (
    <div className="flex min-h-screen items-center justify-center">
      <div className="text-center">
        <h2 className="text-4xl font-bold mb-4">404</h2>
        <p className="text-gray-600">Page not found</p>
      </div>
    </div>
  )
}

// app/global-error.tsx (root error boundary)
'use client'

export default function GlobalError({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  return (
    <html>
      <body>
        <h2>Something went wrong!</h2>
        <button onClick={reset}>Try again</button>
      </body>
    </html>
  )
}
```

### Try-Catch Patterns

```tsx
// Server Component
export default async function UserPage({ params }: { params: { id: string } }) {
  try {
    const user = await db.user.findUniqueOrThrow({
      where: { id: params.id }
    })
    
    return <UserProfile user={user} />
  } catch (error) {
    if (error instanceof Prisma.NotFoundError) {
      notFound() // Triggers not-found.tsx
    }
    
    throw error // Triggers error.tsx
  }
}

// Client Component
'use client'

export function DataFetcher() {
  const [data, setData] = useState(null)
  const [error, setError] = useState<string | null>(null)
  const [loading, setLoading] = useState(true)
  
  useEffect(() => {
    fetch('/api/data')
      .then(res => {
        if (!res.ok) throw new Error('Failed to fetch')
        return res.json()
      })
      .then(setData)
      .catch(err => setError(err.message))
      .finally(() => setLoading(false))
  }, [])
  
  if (loading) return <div>Loading...</div>
  if (error) return <div>Error: {error}</div>
  
  return <div>{JSON.stringify(data)}</div>
}
```

### Custom Error Classes

```ts
// lib/errors.ts
export class AppError extends Error {
  constructor(
    message: string,
    public statusCode: number = 500,
    public code?: string
  ) {
    super(message)
    this.name = 'AppError'
  }
}

export class ValidationError extends AppError {
  constructor(message: string, public errors?: Record<string, string>) {
    super(message, 400, 'VALIDATION_ERROR')
    this.name = 'ValidationError'
  }
}

export class NotFoundError extends AppError {
  constructor(resource: string) {
    super(`${resource} not found`, 404, 'NOT_FOUND')
    this.name = 'NotFoundError'
  }
}

export class UnauthorizedError extends AppError {
  constructor(message = 'Unauthorized') {
    super(message, 401, 'UNAUTHORIZED')
    this.name = 'UnauthorizedError'
  }
}

// Usage in API route
export async function GET(request: NextRequest) {
  try {
    const user = await findUser('123')
    if (!user) throw new NotFoundError('User')
    
    return NextResponse.json({ user })
  } catch (error) {
    if (error instanceof AppError) {
      return NextResponse.json(
        { error: error.message, code: error.code },
        { status: error.statusCode }
      )
    }
    
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    )
  }
}
```

---

## Performance Optimization

### Image Optimization

```tsx
import Image from 'next/image'

// ✅ Use Next.js Image component
export function ProductCard({ product }: { product: Product }) {
  return (
    <div>
      <Image
        src={product.imageUrl}
        alt={product.name}
        width={400}
        height={300}
        placeholder="blur"
        blurDataURL={product.blurDataUrl}
        sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
      />
    </div>
  )
}

// Static images
import logo from '@/public/logo.png'

<Image 
  src={logo} 
  alt="Logo" 
  // width/height automatically inferred
/>
```

### Code Splitting & Lazy Loading

```tsx
// Dynamic imports for client components
import dynamic from 'next/dynamic'

const HeavyChart = dynamic(() => import('@/components/heavy-chart'), {
  loading: () => <div>Loading chart...</div>,
  ssr: false // Disable SSR for this component
})

export function Dashboard() {
  return (
    <div>
      <h1>Dashboard</h1>
      <HeavyChart />
    </div>
  )
}

// Lazy load with React.lazy (client components only)
'use client'

import { lazy, Suspense } from 'react'

const Modal = lazy(() => import('@/components/modal'))

export function Page() {
  const [showModal, setShowModal] = useState(false)
  
  return (
    <div>
      <button onClick={() => setShowModal(true)}>Open Modal</button>
      {showModal && (
        <Suspense fallback={<div>Loading...</div>}>
          <Modal onClose={() => setShowModal(false)} />
        </Suspense>
      )}
    </div>
  )
}
```

### Font Optimization

```tsx
// app/layout.tsx
import { Inter, Roboto_Mono } from 'next/font/google'

const inter = Inter({
  subsets: ['latin'],
  variable: '--font-inter',
  display: 'swap',
})

const robotoMono = Roboto_Mono({
  subsets: ['latin'],
  variable: '--font-mono',
  display: 'swap',
})

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={`${inter.variable} ${robotoMono.variable}`}>
      <body className="font-sans">{children}</body>
    </html>
  )
}
```

### Streaming & Suspense

```tsx
// app/dashboard/page.tsx
import { Suspense } from 'react'

export default function DashboardPage() {
  return (
    <div>
      <h1>Dashboard</h1>
      
      {/* Stream independent sections */}
      <Suspense fallback={<Skeleton />}>
        <RecentOrders />
      </Suspense>
      
      <Suspense fallback={<Skeleton />}>
        <Analytics />
      </Suspense>
    </div>
  )
}

// Async Server Component
async function RecentOrders() {
  const orders = await db.order.findMany({ take: 10 })
  return <OrderList orders={orders} />
}

// app/dashboard/loading.tsx (fallback for whole page)
export default function Loading() {
  return <div>Loading dashboard...</div>
}
```

### Memoization

```tsx
'use client'

import { memo, useMemo, useCallback } from 'react'

// Memoize expensive computations
export function DataTable({ data, filter }: { data: Item[], filter: string }) {
  const filteredData = useMemo(() => {
    return data.filter(item => item.name.includes(filter))
  }, [data, filter])
  
  const handleSort = useCallback((column: string) => {
    // Sort logic
  }, [])
  
  return <Table data={filteredData} onSort={handleSort} />
}

// Memoize component (only re-renders when props change)
export const ExpensiveComponent = memo(function ExpensiveComponent({
  data
}: {
  data: ComplexData
}) {
  // Heavy rendering logic
  return <div>{/* ... */}</div>
})
```

### Parallel Data Fetching

```tsx
// ✅ Parallel requests (faster)
export default async function Page() {
  const [user, posts, comments] = await Promise.all([
    fetchUser(),
    fetchPosts(),
    fetchComments(),
  ])
  
  return <div>...</div>
}

// ❌ Sequential requests (slower)
export default async function Page() {
  const user = await fetchUser()
  const posts = await fetchPosts()      // Waits for user
  const comments = await fetchComments() // Waits for posts
  
  return <div>...</div>
}
```

### Caching Strategies

```tsx
// Force static generation (cached at build time)
export const dynamic = 'force-static'

// Revalidate every 60 seconds
export const revalidate = 60

// Dynamic rendering (opt out of caching)
export const dynamic = 'force-dynamic'

// Per-request caching
export default async function Page() {
  const data = await fetch('https://api.example.com/data', {
    next: { revalidate: 3600 } // Cache for 1 hour
  })
}

// Opt out of caching
const data = await fetch('https://api.example.com/data', {
  cache: 'no-store'
})
```

---

## Git Conventions

### Branch Naming

```bash
# Format: <type>/<short-description>

# Types:
feature/user-authentication
feature/payment-integration

bugfix/login-redirect
bugfix/image-upload

hotfix/security-patch

chore/update-dependencies
chore/refactor-components

docs/update-readme
```

### Commit Messages

Follow **Conventional Commits** format:

```bash
# Format: <type>(<scope>): <subject>

# Types:
feat: add user authentication
feat(auth): implement JWT login

fix: resolve image upload bug
fix(api): handle null user edge case

docs: update README with setup instructions

style: format code with prettier

refactor: restructure component hierarchy
refactor(ui): extract button variants to separate file

perf: optimize image loading

test: add unit tests for auth service

chore: upgrade Next.js to 14.1
chore(deps): update tailwind to 3.4

# Breaking changes:
feat!: migrate to App Router

feat(api)!: change response format
BREAKING CHANGE: API now returns data in { data, meta } format
```

### Commit Best Practices

```bash
# ✅ Small, focused commits
git commit -m "feat(auth): add login form component"
git commit -m "feat(auth): add login API route"
git commit -m "feat(auth): integrate login with state management"

# ❌ Large, unfocused commits
git commit -m "add authentication"

# ✅ Present tense, imperative mood
git commit -m "add feature" # ✅
git commit -m "added feature" # ❌
git commit -m "adds feature" # ❌

# Use commit body for context
git commit -m "fix(api): handle race condition in user creation

Users could create duplicate accounts if they submitted the form
multiple times quickly. Added database constraint and debouncing
to prevent this."
```

### Branching Strategy

```bash
# Main branches
main           # Production-ready code
develop        # Integration branch for features

# Feature workflow
git checkout develop
git checkout -b feature/new-feature
# ... work on feature ...
git commit -m "feat: add new feature"
git push origin feature/new-feature
# Create PR to develop

# Hotfix workflow
git checkout main
git checkout -b hotfix/critical-bug
# ... fix bug ...
git commit -m "fix: resolve critical bug"
git push origin hotfix/critical-bug
# Create PR to main AND develop

# Release workflow
git checkout develop
git checkout -b release/v1.2.0
# ... final testing, version bumps ...
git commit -m "chore: bump version to 1.2.0"
# Merge to main and develop
```

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] Tested locally
- [ ] Added/updated unit tests
- [ ] Added/updated integration tests

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Commented complex logic
- [ ] Updated documentation
- [ ] No new warnings
- [ ] Added tests that prove fix/feature works
- [ ] Dependent changes merged

## Screenshots (if applicable)
```

---

## File Naming & Import Ordering

### File Naming Conventions

```
# Components: PascalCase
UserProfile.tsx
NavigationMenu.tsx
Button.tsx

# Utilities/Hooks: kebab-case
use-auth.ts
use-media-query.ts
format-date.ts
api-client.ts

# Config/Constants: kebab-case
site-config.ts
api-routes.ts

# Types: kebab-case or match component
user-types.ts
types.ts
Button.types.ts (if colocated)

# Tests: match source + .test or .spec
Button.test.tsx
use-auth.test.ts
api-client.spec.ts

# Folders: kebab-case
user-profile/
navigation-menu/
api-routes/
```

### Import Ordering

Order imports by type, with blank lines between groups:

```tsx
// 1. External dependencies (React, third-party)
import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { z } from 'zod'

// 2. Internal absolute imports (@/ alias)
import { Button } from '@/components/ui/button'
import { useAuth } from '@/hooks/use-auth'
import { cn } from '@/lib/utils'
import type { User } from '@/types'

// 3. Relative imports (same directory or parent)
import { UserAvatar } from './user-avatar'
import { calculateAge } from '../utils'

// 4. CSS/Styles
import styles from './component.module.css'

// 5. Types (if using import type syntax)
import type { Props } from './types'
```

### Path Aliases

Configure in `tsconfig.json`:

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./*"],
      "@/components/*": ["./components/*"],
      "@/lib/*": ["./lib/*"],
      "@/hooks/*": ["./hooks/*"],
      "@/types/*": ["./types/*"],
      "@/styles/*": ["./styles/*"]
    }
  }
}
```

### Barrel Exports (index.ts)

Use sparingly. Good for component libraries, avoid for everything else.

```tsx
// components/ui/index.ts
export { Button } from './button'
export { Input } from './input'
export { Card } from './card'

// Usage
import { Button, Input } from '@/components/ui'
```

---

## Environment Variables

### Naming Convention

```bash
# Public variables (exposed to browser): NEXT_PUBLIC_*
NEXT_PUBLIC_API_URL=https://api.example.com
NEXT_PUBLIC_GA_ID=G-XXXXXXXXXX
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_xxx

# Private variables (server-only)
DATABASE_URL=postgresql://...
JWT_SECRET=super-secret
STRIPE_SECRET_KEY=sk_test_xxx
OPENAI_API_KEY=sk-xxx
```

### Environment Files

```bash
# .env.local (gitignored, local development)
DATABASE_URL=postgresql://localhost:5432/dev

# .env.development (committed, development defaults)
NEXT_PUBLIC_API_URL=http://localhost:3000/api

# .env.production (committed, production defaults)
NEXT_PUBLIC_API_URL=https://api.production.com

# .env.example (committed, template for team)
DATABASE_URL=
JWT_SECRET=
NEXT_PUBLIC_API_URL=
```

### Type Safety for Env Variables

```ts
// lib/env.ts
import { z } from 'zod'

const envSchema = z.object({
  DATABASE_URL: z.string().url(),
  JWT_SECRET: z.string().min(32),
  NEXT_PUBLIC_API_URL: z.string().url(),
  NEXT_PUBLIC_GA_ID: z.string().optional(),
})

export const env = envSchema.parse({
  DATABASE_URL: process.env.DATABASE_URL,
  JWT_SECRET: process.env.JWT_SECRET,
  NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL,
  NEXT_PUBLIC_GA_ID: process.env.NEXT_PUBLIC_GA_ID,
})

// Usage (fully typed)
import { env } from '@/lib/env'

const url = env.DATABASE_URL // string, guaranteed to exist
```

### Access Patterns

```tsx
// ✅ Server Component / API Route (access any env var)
export default async function Page() {
  const secret = process.env.JWT_SECRET // OK
  const publicUrl = process.env.NEXT_PUBLIC_API_URL // OK
}

// ✅ Client Component (only NEXT_PUBLIC_* vars)
'use client'

export function Map() {
  const apiKey = process.env.NEXT_PUBLIC_GOOGLE_MAPS_KEY // OK
  const secret = process.env.JWT_SECRET // ❌ undefined
}

// ✅ Build-time access
export async function generateStaticParams() {
  const apiUrl = process.env.NEXT_PUBLIC_API_URL
  const data = await fetch(apiUrl).then(r => r.json())
  return data.map(item => ({ id: item.id }))
}
```

---

## Accessibility

### Semantic HTML

Use the right HTML element for the job.

```tsx
// ✅ Semantic HTML
<header>
  <nav>
    <ul>
      <li><a href="/">Home</a></li>
    </ul>
  </nav>
</header>

<main>
  <article>
    <h1>Article Title</h1>
    <p>Content...</p>
  </article>
  
  <aside>
    <h2>Related Links</h2>
  </aside>
</main>

<footer>
  <p>&copy; 2024 Company</p>
</footer>

// ❌ Divs everywhere
<div className="header">
  <div className="nav">
    <div className="link">Home</div>
  </div>
</div>
```

### ARIA Attributes

```tsx
// Buttons
<button
  aria-label="Close dialog"
  aria-pressed={isPressed}
  aria-expanded={isExpanded}
>
  <XIcon aria-hidden="true" />
</button>

// Links
<a 
  href="/docs"
  aria-current="page" // or "step", "location", "date", "time"
>
  Documentation
</a>

// Images
<Image
  src="/hero.jpg"
  alt="Team collaborating in a modern office"
  aria-describedby="hero-caption"
/>
<p id="hero-caption">Our team working on innovative solutions</p>

// Decorative images (hide from screen readers)
<Image src="/decoration.svg" alt="" aria-hidden="true" />

// Form controls
<label htmlFor="email">Email</label>
<input
  id="email"
  type="email"
  aria-required="true"
  aria-invalid={hasError}
  aria-describedby={hasError ? "email-error" : undefined}
/>
{hasError && <span id="email-error" role="alert">Invalid email</span>}

// Loading states
<div aria-live="polite" aria-busy={isLoading}>
  {isLoading ? 'Loading...' : data}
</div>

// Landmarks
<section aria-labelledby="products-heading">
  <h2 id="products-heading">Our Products</h2>
</section>
```

### Keyboard Navigation

```tsx
'use client'

export function Dropdown() {
  const [isOpen, setIsOpen] = useState(false)
  const triggerRef = useRef<HTMLButtonElement>(null)
  
  useEffect(() => {
    if (!isOpen) return
    
    function handleEscape(e: KeyboardEvent) {
      if (e.key === 'Escape') {
        setIsOpen(false)
        triggerRef.current?.focus()
      }
    }
    
    document.addEventListener('keydown', handleEscape)
    return () => document.removeEventListener('keydown', handleEscape)
  }, [isOpen])
  
  return (
    <div>
      <button
        ref={triggerRef}
        onClick={() => setIsOpen(!isOpen)}
        aria-expanded={isOpen}
        aria-haspopup="true"
      >
        Menu
      </button>
      
      {isOpen && (
        <ul role="menu">
          <li>
            <button role="menuitem" onClick={() => console.log('Item 1')}>
              Item 1
            </button>
          </li>
          <li>
            <button role="menuitem" onClick={() => console.log('Item 2')}>
              Item 2
            </button>
          </li>
        </ul>
      )}
    </div>
  )
}
```

### Focus Management

```tsx
'use client'

import { useRef, useEffect } from 'react'

export function Modal({ isOpen, onClose }: { isOpen: boolean, onClose: () => void }) {
  const closeButtonRef = useRef<HTMLButtonElement>(null)
  const previousFocusRef = useRef<HTMLElement | null>(null)
  
  useEffect(() => {
    if (isOpen) {
      previousFocusRef.current = document.activeElement as HTMLElement
      closeButtonRef.current?.focus()
    } else {
      previousFocusRef.current?.focus()
    }
  }, [isOpen])
  
  if (!isOpen) return null
  
  return (
    <div
      role="dialog"
      aria-modal="true"
      aria-labelledby="modal-title"
      className="fixed inset-0 z-50 flex items-center justify-center"
    >
      <div className="bg-white p-6 rounded-lg">
        <h2 id="modal-title">Modal Title</h2>
        <p>Modal content</p>
        <button ref={closeButtonRef} onClick={onClose}>
          Close
        </button>
      </div>
    </div>
  )
}
```

### Skip Links

```tsx
// app/layout.tsx
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <a 
          href="#main-content" 
          className="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 focus:z-50 focus:px-4 focus:py-2 focus:bg-blue-600 focus:text-white"
        >
          Skip to main content
        </a>
        
        <Header />
        <main id="main-content" tabIndex={-1}>
          {children}
        </main>
        <Footer />
      </body>
    </html>
  )
}

// tailwind.config.js - add sr-only utility
module.exports = {
  theme: {
    extend: {
      // Already included by default
    }
  }
}

// Usage: className="sr-only" hides visually but keeps accessible
```

### Color Contrast

Ensure WCAG AA compliance (4.5:1 for normal text, 3:1 for large text).

```tsx
// ✅ Good contrast
<button className="bg-blue-600 text-white">
  Click me
</button>

// ❌ Poor contrast
<button className="bg-blue-200 text-blue-300">
  Click me
</button>

// Use tools:
// - https://webaim.org/resources/contrastchecker/
// - Chrome DevTools Accessibility panel
```

---

## Security Basics

### Input Validation

Always validate and sanitize user input.

```tsx
import { z } from 'zod'

// Define schema
const userSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8).max(100),
  age: z.number().int().min(0).max(120),
})

// Validate in API route
export async function POST(request: NextRequest) {
  const body = await request.json()
  
  try {
    const validated = userSchema.parse(body)
    // Use validated data
  } catch (error) {
    if (error instanceof z.ZodError) {
      return NextResponse.json(
        { error: 'Invalid input', details: error.errors },
        { status: 400 }
      )
    }
  }
}

// Sanitize HTML (if rendering user content)
import DOMPurify from 'isomorphic-dompurify'

const clean = DOMPurify.sanitize(dirtyHTML)
```

### XSS Prevention

React escapes by default, but be careful with `dangerouslySetInnerHTML`.

```tsx
// ✅ Safe (React escapes automatically)
<div>{userInput}</div>

// ⚠️ Dangerous (only use with sanitized content)
<div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(userInput) }} />

// ❌ Never do this
<div dangerouslySetInnerHTML={{ __html: userInput }} />

// ✅ Safe links
<a href={sanitizeUrl(userUrl)}>Link</a>

function sanitizeUrl(url: string) {
  try {
    const parsed = new URL(url)
    // Only allow http/https
    if (!['http:', 'https:'].includes(parsed.protocol)) {
      return '#'
    }
    return url
  } catch {
    return '#'
  }
}
```

### CSRF Protection

Next.js API routes are protected by default with same-origin policy.

```tsx
// API routes only accept requests from same origin
export async function POST(request: NextRequest) {
  // Additional CSRF token validation (if needed)
  const token = request.headers.get('x-csrf-token')
  
  if (!validateCsrfToken(token)) {
    return NextResponse.json(
      { error: 'Invalid CSRF token' },
      { status: 403 }
    )
  }
  
  // Process request
}

// For external APIs, use CORS headers
export async function GET(request: NextRequest) {
  return NextResponse.json(
    { data: 'public data' },
    {
      headers: {
        'Access-Control-Allow-Origin': 'https://trusted-site.com',
        'Access-Control-Allow-Methods': 'GET, POST',
        'Access-Control-Allow-Headers': 'Content-Type',
      }
    }
  )
}
```

### Authentication Tokens

```tsx
// ✅ Store tokens securely
// Server-side: Use httpOnly cookies
export async function POST(request: NextRequest) {
  const token = generateToken()
  
  const response = NextResponse.json({ success: true })
  response.cookies.set('auth_token', token, {
    httpOnly: true,   // Prevents JS access
    secure: true,     // HTTPS only
    sameSite: 'lax',  // CSRF protection
    maxAge: 60 * 60 * 24 * 7, // 1 week
  })
  
  return response
}

// ❌ Don't store sensitive tokens in localStorage
localStorage.setItem('token', token) // Vulnerable to XSS

// ✅ If you must use client-side storage, encrypt it
import { encrypt, decrypt } from '@/lib/crypto'

const encryptedToken = encrypt(token)
localStorage.setItem('token', encryptedToken)
```

### SQL Injection Prevention

Use parameterized queries / ORMs.

```tsx
// ✅ Using Prisma (safe)
const user = await db.user.findUnique({
  where: { email: userEmail }
})

// ✅ Using parameterized queries
import { sql } from '@vercel/postgres'

const result = await sql`
  SELECT * FROM users WHERE email = ${userEmail}
`

// ❌ String concatenation (vulnerable)
const result = await sql.query(`
  SELECT * FROM users WHERE email = '${userEmail}'
`)
```

### Rate Limiting

```tsx
// lib/rate-limit.ts
import { LRUCache } from 'lru-cache'

type RateLimitOptions = {
  interval: number
  uniqueTokenPerInterval: number
}

export function rateLimit(options: RateLimitOptions) {
  const tokenCache = new LRUCache({
    max: options.uniqueTokenPerInterval,
    ttl: options.interval,
  })

  return {
    check: (token: string, limit: number): boolean => {
      const tokenCount = (tokenCache.get(token) as number) || 0
      
      if (tokenCount >= limit) {
        return false
      }
      
      tokenCache.set(token, tokenCount + 1)
      return true
    },
  }
}

// Usage in API route
const limiter = rateLimit({
  interval: 60 * 1000, // 1 minute
  uniqueTokenPerInterval: 500,
})

export async function POST(request: NextRequest) {
  const ip = request.ip ?? '127.0.0.1'
  
  const isAllowed = limiter.check(ip, 10) // 10 requests per minute
  
  if (!isAllowed) {
    return NextResponse.json(
      { error: 'Rate limit exceeded' },
      { status: 429 }
    )
  }
  
  // Process request
}
```

### Secrets Management

```tsx
// ✅ Never commit secrets
// Use .env.local (gitignored)
DATABASE_URL=postgresql://...
API_KEY=secret

// ✅ Validate secrets at startup
// lib/env.ts
if (!process.env.DATABASE_URL) {
  throw new Error('DATABASE_URL is not set')
}

// ✅ Use environment-specific secrets
// Vercel: Use Environment Variables in dashboard
// Other: Use secrets management service (AWS Secrets Manager, etc.)

// ❌ Never hardcode secrets
const API_KEY = 'sk-1234567890' // DON'T DO THIS

// ❌ Never log secrets
console.log('API Key:', process.env.API_KEY) // DON'T DO THIS
```

---

## Summary

This skill covers the full stack of standards for building production-ready Next.js applications:

1. **File structure** follows App Router conventions
2. **Components** default to Server Components, client only when needed
3. **TypeScript** uses strict mode, types over interfaces, clear naming
4. **Tailwind** uses design tokens, CVA for variants, mobile-first responsive
5. **Patterns** favor composition, custom hooks, and URL state
6. **APIs** follow REST conventions with proper error handling
7. **Errors** are caught at boundaries with graceful fallbacks
8. **Performance** leverages Next.js optimizations (Image, fonts, code splitting)
9. **Git** uses conventional commits and clear branch strategy
10. **Files** use consistent naming and import ordering
11. **Environment** variables are typed and validated
12. **Accessibility** uses semantic HTML, ARIA, and keyboard support
13. **Security** validates input, prevents XSS/CSRF, and protects secrets

Use this as a reference when writing, reviewing, or scaffolding code. Keep it updated as conventions evolve.
