---
name: ui-ux-design
description: >
  UI/UX design principles, component patterns, animations, and Apple-inspired aesthetics for modern web apps.
  Use when: building any user interface, choosing colors/spacing/typography, adding animations, or reviewing UI quality.
  Don't use when: writing backend logic, API routes, or data models (use code-standards instead).
  Don't use when: writing marketing copy or headlines (use copywriting instead).
  Output: Premium, Apple-inspired UI with proper spacing, typography, animation, and accessibility.
---

# UI/UX Design Skill

---

## Quick Reference

| Section | When to Use |
|---------|-------------|
| [Design Principles](#design-principles) | Starting any UI project |
| [Spacing System](#spacing-system) | Layout and positioning |
| [Typography](#typography) | Text styling hierarchy |
| [Color System](#color-system) | Theming and dark mode |
| [Animation Patterns](#animation-patterns) | Adding motion and interactions |
| [Component Patterns](#component-patterns) | Building reusable UI elements |
| [Responsive Design](#responsive-design) | Mobile-first layouts |
| [Accessibility](#accessibility) | Ensuring usability for all |

---

## Design Principles

### Apple-Inspired Aesthetic Rules

**1. Whitespace is a feature, not empty space**
- Generous padding (minimum 24px between sections)
- Content width max 1200px, centered
- Hero sections: 40-60% whitespace
- Let content breathe — cramped = cheap

**2. Visual Hierarchy**
- One primary action per view
- Size contrast: Headlines 2.5-4x body text
- Weight contrast: Bold headlines, regular body
- Color contrast: Primary CTA stands out, secondary muted

**3. Premium Feel Indicators**
- Subtle shadows: `shadow-sm` to `shadow-lg`, never harsh
- Rounded corners: 8-16px standard, 24px for cards
- Transitions on everything interactive: 150-300ms
- No harsh borders — use shadows and backgrounds instead

**4. Minimalism Rules**
- Remove elements until it breaks, then add one back
- Every element must earn its place
- Icons > text labels when meaning is clear
- Progressive disclosure — hide advanced options

### Tailwind Config for Apple Aesthetic

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'SF Pro Display', 'system-ui', 'sans-serif'],
      },
      spacing: {
        '18': '4.5rem',
        '22': '5.5rem',
        '30': '7.5rem',
      },
      borderRadius: {
        '4xl': '2rem',
      },
      boxShadow: {
        'soft': '0 2px 15px -3px rgba(0, 0, 0, 0.07), 0 10px 20px -2px rgba(0, 0, 0, 0.04)',
        'glow': '0 0 40px rgba(99, 102, 241, 0.15)',
      },
    },
  },
}
```

---

## Spacing System

### The 8px Grid

All spacing uses multiples of 8px. This creates visual rhythm and consistency.

| Token | Value | Use Case |
|-------|-------|----------|
| `space-1` | 4px | Tight spacing, icon gaps |
| `space-2` | 8px | Related elements |
| `space-3` | 12px | Component internal padding |
| `space-4` | 16px | Default component padding |
| `space-6` | 24px | Section internal gaps |
| `space-8` | 32px | Between related sections |
| `space-12` | 48px | Major section breaks |
| `space-16` | 64px | Page section dividers |
| `space-24` | 96px | Hero/content separation |

### Component Padding Standards

```jsx
// Buttons
<button className="px-4 py-2">Small</button>
<button className="px-6 py-3">Default</button>
<button className="px-8 py-4">Large</button>

// Cards
<div className="p-6">Standard card</div>
<div className="p-8">Featured card</div>
<div className="p-4">Compact card</div>

// Page sections
<section className="py-16 md:py-24">Standard section</section>
<section className="py-24 md:py-32">Hero section</section>
```

---

## Typography

### Scale (Type-safe sizes)

| Element | Size | Weight | Line Height |
|---------|------|--------|-------------|
| Display | `text-6xl` (60px) | 700 | 1.1 |
| H1 | `text-5xl` (48px) | 700 | 1.2 |
| H2 | `text-4xl` (36px) | 600 | 1.25 |
| H3 | `text-2xl` (24px) | 600 | 1.3 |
| H4 | `text-xl` (20px) | 600 | 1.4 |
| Body | `text-base` (16px) | 400 | 1.6 |
| Small | `text-sm` (14px) | 400 | 1.5 |
| Caption | `text-xs` (12px) | 500 | 1.4 |

### Typography Rules

```jsx
// Headline hierarchy
<h1 className="text-4xl md:text-5xl lg:text-6xl font-bold tracking-tight">
  Main Headline
</h1>

// Subheadline — lighter weight, larger size than body
<p className="text-xl md:text-2xl text-gray-600 dark:text-gray-400 font-normal">
  Supporting text that explains the headline
</p>

// Body text — comfortable reading width
<p className="text-base text-gray-700 dark:text-gray-300 leading-relaxed max-w-prose">
  Body content goes here. Max width 65ch for readability.
</p>

// Label/caption
<span className="text-xs font-medium uppercase tracking-wide text-gray-500">
  Category
</span>
```

### Letter Spacing

- Headlines: `tracking-tight` (-0.025em)
- Body: `tracking-normal`
- Labels/Caps: `tracking-wide` (0.025em) or `tracking-wider` (0.05em)

---

## Color System

### Dark Mode Palette (Primary for Tyler's Apps)

```css
/* Base dark theme */
--bg-primary: #0a0a0a;      /* Main background */
--bg-secondary: #141414;    /* Card backgrounds */
--bg-tertiary: #1a1a1a;     /* Elevated surfaces */
--bg-hover: #242424;        /* Hover states */

--text-primary: #ffffff;     /* Headlines */
--text-secondary: #a3a3a3;   /* Body text */
--text-muted: #737373;       /* Captions, placeholders */

--border-subtle: #262626;    /* Subtle dividers */
--border-default: #404040;   /* Visible borders */

--accent-primary: #818cf8;   /* Primary action (indigo) */
--accent-secondary: #34d399; /* Success states */
--accent-warning: #fbbf24;   /* Warning states */
--accent-danger: #f87171;    /* Error states */
```

### Tailwind Dark Mode Setup

```jsx
// tailwind.config.js
module.exports = {
  darkMode: 'class', // Manual toggle via class
  theme: {
    extend: {
      colors: {
        dark: {
          50: '#18181b',
          100: '#1f1f23',
          200: '#27272a',
          300: '#3f3f46',
          400: '#52525b',
          500: '#71717a',
          600: '#a1a1aa',
          700: '#d4d4d8',
          800: '#e4e4e7',
          900: '#f4f4f5',
        },
      },
    },
  },
}
```

### Color Usage Rules

1. **Backgrounds:** Start dark, go lighter for elevation
   ```jsx
   <div className="bg-zinc-950"> {/* Page */}
     <div className="bg-zinc-900"> {/* Card */}
       <div className="bg-zinc-800"> {/* Input/hover */}
   ```

2. **Text:** High contrast for primary, muted for secondary
   ```jsx
   <h2 className="text-white">Primary text</h2>
   <p className="text-zinc-400">Secondary text</p>
   <span className="text-zinc-500">Muted text</span>
   ```

3. **Accents:** Use sparingly, one primary accent color
   ```jsx
   <button className="bg-indigo-500 hover:bg-indigo-400">
     Primary Action
   </button>
   ```

### Theme Toggle Implementation

```jsx
// components/ThemeToggle.tsx
'use client'
import { useEffect, useState } from 'react'

export function useTheme() {
  const [theme, setTheme] = useState<'light' | 'dark' | 'system'>('dark')
  
  useEffect(() => {
    const stored = localStorage.getItem('theme') as 'light' | 'dark' | 'system' | null
    if (stored) setTheme(stored)
  }, [])
  
  useEffect(() => {
    const root = document.documentElement
    const isDark = theme === 'dark' || 
      (theme === 'system' && window.matchMedia('(prefers-color-scheme: dark)').matches)
    
    root.classList.toggle('dark', isDark)
    localStorage.setItem('theme', theme)
  }, [theme])
  
  return { theme, setTheme }
}
```

---

## Animation Patterns

### Animation Philosophy

1. **Purpose over decoration** — Every animation must serve a purpose
2. **Fast but noticeable** — 150-300ms for micro, 300-500ms for transitions
3. **Natural easing** — Use spring physics or ease-out curves
4. **Respect user preferences** — Check `prefers-reduced-motion`

### Core Animation Timings

| Type | Duration | Easing |
|------|----------|--------|
| Micro-interaction (hover) | 150ms | ease-out |
| Small transition | 200ms | ease-out |
| Medium transition | 300ms | ease-out |
| Large transition (page) | 400-500ms | ease-in-out |
| Spring animations | stiffness: 300, damping: 30 | spring |

---

### Framer Motion Patterns

#### 1. Scroll-Triggered Fade In

```jsx
import { motion, useInView } from 'motion/react'
import { useRef } from 'react'

function FadeInSection({ children, delay = 0 }) {
  const ref = useRef(null)
  const isInView = useInView(ref, { once: true, margin: '-100px' })
  
  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 30 }}
      animate={isInView ? { opacity: 1, y: 0 } : { opacity: 0, y: 30 }}
      transition={{ duration: 0.5, delay, ease: 'easeOut' }}
    >
      {children}
    </motion.div>
  )
}
```

#### 2. Staggered List Animation

```jsx
import { motion } from 'motion/react'

const container = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1,
      delayChildren: 0.2,
    },
  },
}

const item = {
  hidden: { opacity: 0, y: 20 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.4, ease: 'easeOut' }
  },
}

function AnimatedList({ items }) {
  return (
    <motion.ul
      variants={container}
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true, margin: '-50px' }}
    >
      {items.map((item, i) => (
        <motion.li key={i} variants={item}>
          {item}
        </motion.li>
      ))}
    </motion.ul>
  )
}
```

#### 3. Button Hover & Tap

```jsx
import { motion } from 'motion/react'

function AnimatedButton({ children, onClick }) {
  return (
    <motion.button
      onClick={onClick}
      whileHover={{ scale: 1.02, y: -2 }}
      whileTap={{ scale: 0.98 }}
      transition={{ type: 'spring', stiffness: 400, damping: 17 }}
      className="px-6 py-3 bg-indigo-500 text-white rounded-xl font-medium"
    >
      {children}
    </motion.button>
  )
}
```

#### 4. Page Transitions

```jsx
// app/layout.tsx or _app.tsx
import { AnimatePresence, motion } from 'motion/react'
import { useRouter } from 'next/router'

const pageVariants = {
  initial: { opacity: 0, y: 20 },
  enter: { opacity: 1, y: 0 },
  exit: { opacity: 0, y: -20 },
}

function MyApp({ Component, pageProps }) {
  const router = useRouter()
  
  return (
    <AnimatePresence mode="wait">
      <motion.div
        key={router.pathname}
        variants={pageVariants}
        initial="initial"
        animate="enter"
        exit="exit"
        transition={{ duration: 0.3, ease: 'easeInOut' }}
      >
        <Component {...pageProps} />
      </motion.div>
    </AnimatePresence>
  )
}
```

#### 5. Modal/Dialog Animation

```jsx
import { motion, AnimatePresence } from 'motion/react'

const overlayVariants = {
  hidden: { opacity: 0 },
  visible: { opacity: 1 },
}

const modalVariants = {
  hidden: { opacity: 0, scale: 0.95, y: 20 },
  visible: { 
    opacity: 1, 
    scale: 1, 
    y: 0,
    transition: { type: 'spring', stiffness: 300, damping: 25 }
  },
  exit: { 
    opacity: 0, 
    scale: 0.95, 
    y: 20,
    transition: { duration: 0.2 }
  },
}

function Modal({ isOpen, onClose, children }) {
  return (
    <AnimatePresence>
      {isOpen && (
        <motion.div
          className="fixed inset-0 bg-black/60 backdrop-blur-sm z-50"
          variants={overlayVariants}
          initial="hidden"
          animate="visible"
          exit="hidden"
          onClick={onClose}
        >
          <motion.div
            variants={modalVariants}
            initial="hidden"
            animate="visible"
            exit="exit"
            className="fixed inset-0 flex items-center justify-center p-4"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="bg-zinc-900 rounded-2xl p-6 max-w-lg w-full shadow-2xl border border-zinc-800">
              {children}
            </div>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  )
}
```

#### 6. Card Hover Effects

```jsx
import { motion } from 'motion/react'

function HoverCard({ children }) {
  return (
    <motion.div
      whileHover={{ 
        y: -8, 
        boxShadow: '0 20px 40px rgba(0,0,0,0.3)',
      }}
      transition={{ type: 'spring', stiffness: 300, damping: 20 }}
      className="bg-zinc-900 rounded-2xl p-6 border border-zinc-800 cursor-pointer"
    >
      {children}
    </motion.div>
  )
}

// With 3D tilt effect
function TiltCard({ children }) {
  return (
    <motion.div
      whileHover={{
        rotateX: 5,
        rotateY: 5,
        scale: 1.02,
      }}
      style={{ transformPerspective: 1000 }}
      transition={{ type: 'spring', stiffness: 300, damping: 20 }}
      className="bg-zinc-900 rounded-2xl p-6"
    >
      {children}
    </motion.div>
  )
}
```

#### 7. Shared Element Transitions (Magic Motion)

```jsx
import { motion, AnimatePresence } from 'motion/react'

function ImageGallery({ images, selectedId, onSelect }) {
  return (
    <>
      {images.map((img) => (
        <motion.div
          key={img.id}
          layoutId={`image-${img.id}`}
          onClick={() => onSelect(img.id)}
          className="cursor-pointer"
        >
          <img src={img.thumb} alt="" />
        </motion.div>
      ))}
      
      <AnimatePresence>
        {selectedId && (
          <motion.div
            layoutId={`image-${selectedId}`}
            className="fixed inset-0 z-50 flex items-center justify-center bg-black/90"
            onClick={() => onSelect(null)}
          >
            <motion.img
              src={images.find(i => i.id === selectedId)?.full}
              className="max-w-4xl max-h-[80vh] rounded-2xl"
            />
          </motion.div>
        )}
      </AnimatePresence>
    </>
  )
}
```

---

### GSAP ScrollTrigger Patterns

Use GSAP for complex scroll-based storytelling. For simpler animations, stick with Framer Motion.

#### Basic Scroll-Triggered Animation

```jsx
import { useEffect, useRef } from 'react'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

function ScrollSection() {
  const sectionRef = useRef(null)
  
  useEffect(() => {
    const ctx = gsap.context(() => {
      gsap.from('.fade-element', {
        scrollTrigger: {
          trigger: sectionRef.current,
          start: 'top 80%',
          end: 'bottom 20%',
          toggleActions: 'play none none reverse',
        },
        opacity: 0,
        y: 50,
        duration: 0.8,
        stagger: 0.2,
      })
    }, sectionRef)
    
    return () => ctx.revert()
  }, [])
  
  return (
    <section ref={sectionRef}>
      <div className="fade-element">Element 1</div>
      <div className="fade-element">Element 2</div>
    </section>
  )
}
```

#### Scrub Animation (Linked to Scroll Position)

```jsx
function ParallaxSection() {
  const sectionRef = useRef(null)
  
  useEffect(() => {
    const ctx = gsap.context(() => {
      gsap.to('.parallax-bg', {
        scrollTrigger: {
          trigger: sectionRef.current,
          start: 'top bottom',
          end: 'bottom top',
          scrub: 1, // Smooth scrubbing, takes 1s to catch up
        },
        y: -200,
        ease: 'none',
      })
      
      // Pinned section with scrub
      gsap.to('.pinned-content', {
        scrollTrigger: {
          trigger: sectionRef.current,
          pin: true,
          start: 'top top',
          end: '+=500',
          scrub: 1,
        },
        x: 400,
      })
    }, sectionRef)
    
    return () => ctx.revert()
  }, [])
  
  return <section ref={sectionRef}>...</section>
}
```

---

### CSS Animation Patterns

#### Fade In Up (No Library)

```css
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in-up {
  animation: fadeInUp 0.5s ease-out forwards;
}

/* With delay utility */
.animation-delay-200 {
  animation-delay: 200ms;
}
```

#### Hover Glow Effect

```css
.hover-glow {
  transition: box-shadow 0.3s ease;
}

.hover-glow:hover {
  box-shadow: 0 0 30px rgba(99, 102, 241, 0.3);
}
```

#### Shimmer Loading Effect

```css
@keyframes shimmer {
  0% {
    background-position: -200% 0;
  }
  100% {
    background-position: 200% 0;
  }
}

.skeleton {
  background: linear-gradient(
    90deg,
    #27272a 25%,
    #3f3f46 50%,
    #27272a 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}
```

---

### Intersection Observer Hook (Vanilla Scroll Trigger)

```jsx
import { useEffect, useRef, useState } from 'react'

function useScrollTrigger(options = {}) {
  const ref = useRef(null)
  const [isInView, setIsInView] = useState(false)
  
  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsInView(true)
          if (options.once) observer.disconnect()
        } else if (!options.once) {
          setIsInView(false)
        }
      },
      {
        threshold: options.threshold || 0.1,
        rootMargin: options.rootMargin || '0px',
      }
    )
    
    if (ref.current) observer.observe(ref.current)
    
    return () => observer.disconnect()
  }, [options.once, options.threshold, options.rootMargin])
  
  return { ref, isInView }
}

// Usage
function MyComponent() {
  const { ref, isInView } = useScrollTrigger({ once: true, rootMargin: '-100px' })
  
  return (
    <div
      ref={ref}
      className={`transition-all duration-500 ${
        isInView ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-8'
      }`}
    >
      Content
    </div>
  )
}
```

---

## Component Patterns

### Button Variants

```jsx
// components/Button.tsx
import { motion } from 'motion/react'
import { cn } from '@/lib/utils'

const variants = {
  primary: 'bg-indigo-500 text-white hover:bg-indigo-400',
  secondary: 'bg-zinc-800 text-white hover:bg-zinc-700',
  ghost: 'bg-transparent text-zinc-300 hover:bg-zinc-800 hover:text-white',
  danger: 'bg-red-500 text-white hover:bg-red-400',
}

const sizes = {
  sm: 'px-3 py-1.5 text-sm rounded-lg',
  md: 'px-4 py-2 text-base rounded-xl',
  lg: 'px-6 py-3 text-lg rounded-xl',
}

export function Button({ 
  variant = 'primary', 
  size = 'md', 
  className,
  children,
  ...props 
}) {
  return (
    <motion.button
      whileHover={{ scale: 1.02 }}
      whileTap={{ scale: 0.98 }}
      className={cn(
        'font-medium transition-colors',
        variants[variant],
        sizes[size],
        className
      )}
      {...props}
    >
      {children}
    </motion.button>
  )
}
```

### Card Component

```jsx
// components/Card.tsx
import { motion } from 'motion/react'
import { cn } from '@/lib/utils'

export function Card({ 
  children, 
  className, 
  hoverable = true,
  onClick 
}) {
  return (
    <motion.div
      onClick={onClick}
      whileHover={hoverable ? { y: -4, boxShadow: '0 20px 40px rgba(0,0,0,0.2)' } : {}}
      transition={{ type: 'spring', stiffness: 300, damping: 20 }}
      className={cn(
        'bg-zinc-900 rounded-2xl p-6 border border-zinc-800',
        hoverable && 'cursor-pointer',
        className
      )}
    >
      {children}
    </motion.div>
  )
}
```

### Input Component

```jsx
// components/Input.tsx
import { cn } from '@/lib/utils'

export function Input({ label, error, className, ...props }) {
  return (
    <div className="space-y-2">
      {label && (
        <label className="text-sm font-medium text-zinc-300">
          {label}
        </label>
      )}
      <input
        className={cn(
          'w-full px-4 py-3 bg-zinc-800 border border-zinc-700 rounded-xl',
          'text-white placeholder:text-zinc-500',
          'focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent',
          'transition-all duration-200',
          error && 'border-red-500',
          className
        )}
        {...props}
      />
      {error && (
        <p className="text-sm text-red-400">{error}</p>
      )}
    </div>
  )
}
```

### Navigation Header

```jsx
// components/Header.tsx
import { motion } from 'motion/react'
import { useState } from 'react'

export function Header() {
  const [scrolled, setScrolled] = useState(false)
  
  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 20)
    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])
  
  return (
    <motion.header
      className={cn(
        'fixed top-0 left-0 right-0 z-50 transition-all duration-300',
        scrolled 
          ? 'bg-zinc-900/80 backdrop-blur-xl border-b border-zinc-800' 
          : 'bg-transparent'
      )}
    >
      <nav className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
        <Logo />
        <Navigation />
        <CTAButton />
      </nav>
    </motion.header>
  )
}
```

---

## Responsive Design

### Mobile-First Breakpoints

```js
// tailwind.config.js
module.exports = {
  theme: {
    screens: {
      'sm': '640px',   // Small tablets
      'md': '768px',   // Tablets
      'lg': '1024px',  // Small laptops
      'xl': '1280px',  // Desktops
      '2xl': '1536px', // Large screens
    },
  },
}
```

### Responsive Patterns

#### Hero Section

```jsx
function Hero() {
  return (
    <section className="min-h-screen flex items-center px-6 py-20 md:py-32">
      <div className="max-w-7xl mx-auto w-full">
        <h1 className="text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-bold tracking-tight">
          Headline
        </h1>
        <p className="mt-6 text-lg md:text-xl lg:text-2xl text-zinc-400 max-w-2xl">
          Subheadline text
        </p>
        <div className="mt-8 flex flex-col sm:flex-row gap-4">
          <Button>Primary CTA</Button>
          <Button variant="secondary">Secondary</Button>
        </div>
      </div>
    </section>
  )
}
```

#### Responsive Grid

```jsx
// 1 col mobile → 2 col tablet → 3 col desktop
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  {items.map(item => <Card key={item.id}>{item}</Card>)}
</div>

// 2 col mobile → 4 col desktop
<div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
  {items.map(...)}
</div>
```

#### Responsive Typography Scale

```jsx
// Responsive text sizing
<h1 className="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-bold">
  Scalable Headline
</h1>

// Consistent vertical rhythm
<section className="py-12 sm:py-16 md:py-20 lg:py-24">
  Content
</section>
```

### Touch Targets

- Minimum 44px tap target for mobile
- Adequate spacing between interactive elements

```jsx
<button className="min-h-[44px] min-w-[44px] px-4 py-3">
  Touch Friendly
</button>
```

---

## Accessibility

### Core Rules (Don't Skip!)

1. **Semantic HTML**
   ```jsx
   // Good
   <nav><ul><li><a href="/">Home</a></li></ul></nav>
   <main><article><h1>Title</h1><p>Content</p></article></main>
   
   // Bad
   <div onClick={navigate}>Home</div>
   ```

2. **Focus States**
   ```css
   .focus-visible:focus {
     outline: 2px solid var(--accent);
     outline-offset: 2px;
   }
   ```
   
   ```jsx
   <button className="focus:ring-2 focus:ring-indigo-500 focus:outline-none">
     Click Me
   </button>
   ```

3. **Color Contrast**
   - Normal text: 4.5:1 minimum
   - Large text: 3:1 minimum
   - Use tools: Stark, contrast-checker

4. **Alt Text for Images**
   ```jsx
   <img src="chart.png" alt="Q4 revenue increased 23% year over year" />
   // Not: alt="image" or alt="chart"
   ```

5. **Form Labels**
   ```jsx
   <label htmlFor="email">Email</label>
   <input id="email" type="email" aria-describedby="email-hint" />
   <p id="email-hint">We'll never share your email</p>
   ```

6. **Skip Links**
   ```jsx
   <a href="#main-content" className="sr-only focus:not-sr-only">
     Skip to main content
   </a>
   ```

### Motion Preferences

```jsx
// Respect reduced motion preference
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches

<motion.div
  initial={{ opacity: 0 }}
  animate={{ opacity: 1 }}
  transition={{ duration: prefersReducedMotion ? 0 : 0.5 }}
>
  Content
</motion.div>

// Or in Tailwind
<div className="motion-reduce:transition-none transition-all duration-300">
```

### ARIA When Needed

```jsx
// Button with loading state
<button 
  aria-busy={isLoading}
  aria-disabled={isLoading}
>
  {isLoading ? 'Saving...' : 'Save'}
</button>

// Modal
<div 
  role="dialog" 
  aria-modal="true" 
  aria-labelledby="modal-title"
>
  <h2 id="modal-title">Modal Title</h2>
</div>

// Expandable accordion
<button
  aria-expanded={isOpen}
  aria-controls="panel-id"
>
  Toggle
</button>
<div id="panel-id" hidden={!isOpen}>
  Content
</div>
```

---

## Dark Mode Design Rules

### Elevation System (Darker = Lower)

```
Level 0: #0a0a0a - Base/background
Level 1: #141414 - Cards, elevated surfaces
Level 2: #1f1f1f - Modals, dropdowns
Level 3: #2a2a2a - Hover states, active items
```

### Text Contrast

- Primary text on dark: `#ffffff` or `#f4f4f5` (zinc-100)
- Secondary text: `#a1a1aa` (zinc-400)
- Muted text: `#71717a` (zinc-500)
- Never use pure black text on dark backgrounds

### Accent Colors for Dark Mode

- Prefer lighter/more saturated accents
- Avoid desaturated colors that blend with dark backgrounds
- Test accent colors against multiple dark backgrounds

### Shadows in Dark Mode

```css
/* Dark mode shadows are subtle, using black */
.shadow-dark {
  box-shadow: 
    0 4px 6px -1px rgba(0, 0, 0, 0.3),
    0 2px 4px -2px rgba(0, 0, 0, 0.3);
}

/* Glow shadows for accent elements */
.glow-accent {
  box-shadow: 0 0 20px rgba(99, 102, 241, 0.3);
}
```

---

## Performance Tips

### Animation Performance

1. **Transform only** — Animate `transform` and `opacity`, not layout properties
2. **Will-change sparingly** — Use only for known animations
3. **Avoid animating filters** — Expensive on low-end devices
4. **Use layout prop in Framer Motion** — Hardware accelerated

```jsx
// Good - transforms
<motion.div animate={{ x: 100, scale: 1.1, opacity: 0.8 }} />

// Bad - layout properties (causes reflow)
<motion.div animate={{ width: 200, padding: 20, margin: 10 }} />

// If you need layout animation, use layout prop
<motion.div layout style={{ width: isExpanded ? '100%' : '50%' }} />
```

### Loading States

```jsx
// Skeleton with animation
function CardSkeleton() {
  return (
    <div className="bg-zinc-900 rounded-2xl p-6 animate-pulse">
      <div className="h-4 bg-zinc-800 rounded w-3/4 mb-4" />
      <div className="h-3 bg-zinc-800 rounded w-1/2" />
    </div>
  )
}
```

---

## Quick Copy Patterns

### Standard Page Layout

```jsx
export default function Page() {
  return (
    <div className="min-h-screen bg-zinc-950 text-white">
      <Header />
      <main className="max-w-7xl mx-auto px-6 py-12 md:py-20">
        {/* Hero */}
        <section className="mb-24">
          <FadeInSection>
            <h1 className="text-4xl md:text-6xl font-bold tracking-tight mb-6">
              Page Title
            </h1>
            <p className="text-xl text-zinc-400 max-w-2xl">
              Supporting description text
            </p>
          </FadeInSection>
        </section>
        
        {/* Content */}
        <section className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {items.map((item, i) => (
            <FadeInSection key={item.id} delay={i * 0.1}>
              <Card>{item}</Card>
            </FadeInSection>
          ))}
        </section>
      </main>
      <Footer />
    </div>
  )
}
```

### Feature Section with Animation

```jsx
function FeatureSection() {
  return (
    <section className="py-24 md:py-32">
      <div className="max-w-7xl mx-auto px-6">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.5 }}
          className="text-center mb-16"
        >
          <h2 className="text-3xl md:text-5xl font-bold mb-4">
            Feature Title
          </h2>
          <p className="text-xl text-zinc-400 max-w-2xl mx-auto">
            Feature description
          </p>
        </motion.div>
        
        <div className="grid md:grid-cols-3 gap-8">
          {features.map((feature, i) => (
            <motion.div
              key={feature.id}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.1, duration: 0.4 }}
            >
              <Card hoverable>
                <div className="w-12 h-12 bg-indigo-500/20 rounded-xl flex items-center justify-center mb-4">
                  <feature.icon className="w-6 h-6 text-indigo-400" />
                </div>
                <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
                <p className="text-zinc-400">{feature.description}</p>
              </Card>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
```

---

## Checklist Before Shipping

- [ ] All interactive elements have hover/focus states
- [ ] Animations respect `prefers-reduced-motion`
- [ ] Touch targets are minimum 44px on mobile
- [ ] Images have meaningful alt text
- [ ] Color contrast meets WCAG AA (4.5:1)
- [ ] Forms have proper labels and error states
- [ ] Page is keyboard navigable
- [ ] Dark mode looks intentional, not inverted
- [ ] Animations feel purposeful, not distracting
- [ ] Mobile experience matches desktop quality
- [ ] Loading states exist for async content
- [ ] Page transitions feel smooth

---

*Last updated: February 2026*
*Stack: Next.js 15+, React 19, Tailwind CSS 4, Framer Motion 12*
