#!/usr/bin/env python3
"""
BytesAndBlessings Blog - Comprehensive Post Fixer
Fixes: empty posts, duplicates, nested figures, meta descriptions, URL typos
"""

import os
import re
import json
import shutil

POSTS_DIR = os.path.expanduser("~/Factory/BytesAndBlessings/site/content/posts")

# ============================================================
# 1. META DESCRIPTIONS for all posts
# ============================================================
META_DESCRIPTIONS = {
    "8020.md": "Discover how the Pareto Principle (80/20 rule) applies across life, business, and productivity. Focus on the vital few to achieve outsized results.",
    "a-soulful-trip-to-vijayawada-annavaram-dwaraka-tirumala.md": "A spiritual road trip through Andhra Pradesh visiting Vijayawada, Annavaram, and Dwaraka Tirumala — temples, prayers, and divine encounters.",
    "are-you-a-multiplier.md": "Are you a Multiplier or a Diminisher? Explore the leadership traits that amplify team intelligence versus those that shut it down.",
    "august-aura-pilgrimage-to-sacred-marvels.md": "A sacred pilgrimage to Shirdi, BhimaShankar, Grishneshwar, and Triambakeshwar — exploring Maharashtra's Jyotirlingas and spiritual heritage.",
    "bad-code-smells.md": "Identify the five categories of bad code smells — Bloaters, Object-Orientation Abusers, Change Preventers, Dispensables, and Couplers.",
    "burning-out.md": "Recognize the warning signs of burnout — from lost motivation to irritability — and learn practical steps to recover before it's too late.",
    "career-sutras.md": "Feeling stuck in your career? These career sutras cover growth strategies from communication mastery to building influence at work.",
    "creating-problems-that-werent-there.md": "Why does the human brain create problems that don't exist? Understand how overthinking manufactures stress and learn to break the cycle.",
    "detox-your-thoughts.md": "A practical guide to detoxing negative thoughts, uncomfortable feelings, and mental traps to improve your total well-being.",
    "e-go.md": "The ego is your worst enemy. Learn how ego blocks growth, damages relationships, and prevents you from reaching your true potential.",
    "expanding-columns-in-wpf.md": "How to dynamically expand DataGrid column height in WPF to handle multi-line cell content using RowDetails and custom templates.",
    "faster.md": "Five principles to accelerate your learning — drop the ego, set stretch goals, stay consistent, and make it fun.",
    "go-lang.md": "An introduction to Go (Golang) — Google's statically typed compiled language known for simplicity, concurrency support, and fast performance.",
    "goddess-parvati.md": "Explore the divine forms of Goddess Parvati — from gentle Uma to fierce Kali — and her significance in Hindu mythology and spirituality.",
    "habits.md": "Five energizing habits versus five draining ones. Master self-discipline, invest in education, and cut the habits holding you back.",
    "hello-world.md": "The first post of Bytes & Blessings — a blog at the crossroads of technology and tradition. Every journey starts with Hello World.",
    "how-browsers-work.md": "A deep dive into how web browsers work — from parsing HTML and CSS to rendering the DOM tree, layout, and painting pixels on screen.",
    "hyper-f0cus.md": "Our attention is overwhelmed like never before. Learn the science of hyperfocus and practical techniques to reclaim deep concentration.",
    "java-architecture.md": "Understanding Java's architecture — the JVM, class loader, bytecode, garbage collection, and how Java achieves platform independence.",
    "javascript.md": "A comprehensive JavaScript reference covering types, objects, functions, closures, prototypes, async patterns, and best practices.",
    "junit-testing-and-best-practices.md": "What is unit testing and why does it matter? Learn JUnit best practices, test structure, and how to write effective automated tests.",
    "kubernetes-learning-path.md": "Why Kubernetes? An introduction to container orchestration — automating deployment, scaling, and management of containerized applications.",
    "kuberneties-learning-path-components.md": "Understanding Kubernetes cluster components — Control Plane, Nodes, kube-apiserver, etcd, scheduler, and how they work together.",
    "kuberneties-learning-path-deployments.md": "Kubernetes Deployments explained — declarative updates, rolling deployments, rollbacks, and managing application lifecycle at scale.",
    "kuberneties-learning-path-pods.md": "What are Kubernetes Pods? The smallest deployable units — understanding pod lifecycle, multi-container pods, networking, and storage.",
    "kuberneties-learning-path-replicaset.md": "Kubernetes ReplicaSets maintain a stable set of replica Pods. Learn how they ensure availability and handle pod failures automatically.",
    "mahalaya-paksham.md": "Understanding Mahalaya Paksham — the sacred fortnight dedicated to honoring ancestors through Tarpanam rituals in Hindu tradition.",
    "navigating-the-stars-understanding-shasta-graha-kutami.md": "What is Shasta Graha Kutami? Understanding the rare six-planet alignment in Vedic astrology and its spiritual significance.",
    "ood-design-patterns-and-anti-patterns.md": "A comprehensive guide to OOD — SOLID principles, Creational, Structural, and Behavioral design patterns, plus anti-patterns to avoid.",
    "overthinking.md": "Why do we overthink and how does it harm us? Practical strategies to break the overthinking cycle and find mental clarity.",
    "power-of-four-for-good-life.md": "The Power of Four framework for living a fulfilling life — balancing happiness, purpose, relationships, and personal growth.",
    "power-of-subconscious-mind.md": "Unlock the treasure house of infinity within you. Key insights from The Power of Your Subconscious Mind on harnessing mental power.",
    "pune-in-march-2025.md": "Exploring Pune's temples and culture in March 2025 — from Dagdusheth Halwai Ganpati to local food trails and peaceful moments.",
    "purpose-and-happiness.md": "What is happiness and how do we find purpose? Exploring the subjective nature of positive emotions and what truly fulfills us.",
    "refactoring-techniques.md": "Essential refactoring techniques — Extract Method, Inline Method, Replace Temp with Query, and more ways to clean up your codebase.",
    "rest-details.md": "A detailed guide to REST APIs — principles, HTTP methods, status codes, HATEOAS, versioning, and best practices for building web services.",
    "scatter-f0cus.md": "The surprising benefits of a wandering mind — how scatter focus boosts creativity, problem-solving, and connects disparate ideas.",
    "security-attacks.md": "Understanding common security attacks — DDoS, SQL Injection, XSS, CSRF, Man-in-the-Middle, and how to defend against them.",
    "service-oriented-architecture.md": "Service-Oriented Architecture (SOA) explained — principles, benefits, governance, and how loosely-coupled services meet business needs.",
    "signs-of-strong-mindset.md": "Six signs of a strong mindset — moving on, embracing change, staying happy, being kind, taking calculated risks, and celebrating others.",
    "socketio-real-time-applications.md": "Building real-time web applications with Socket.IO — WebSockets, event-driven architecture, and practical implementation patterns.",
    "software-architecture-what.md": "Software architecture fundamentals — defining structured solutions that balance technical requirements with quality attributes like performance and security.",
    "start-living.md": "Five life principles to stop existing and start truly living — embrace mistakes, master self-talk, and let go of the past.",
    "stop-pleasing.md": "Why people-pleasing undermines your authenticity. True personalities don't seek external approval — they live on their own terms.",
    "tarpanam-introduction.md": "తర్పణం (Tarpanam) — understanding the sacred ritual of offering water to ancestors, its spiritual significance, and how to perform it.",
    "temple-trip-across-tamil-nadu.md": "Four days across Tamil Nadu visiting ancient temples — Meenakshi, Ramanathaswamy, Thanjavur, and more. A journey of faith and discovery.",
    "unfuck-yourself.md": "Key insights from Unf*ck Yourself — how self-talk shapes your reality, and practical strategies to break free from limiting beliefs.",
    "unit-testing-what-why-how.md": "A complete guide to unit testing — what it is, why it matters, testing frameworks, best practices, and how to write tests that actually help.",
    "varanasi-in-february-2025.md": "Visiting Varanasi during Maha Kumbh 2025 — ghats, temples, the Ganga Aarti, and the spiritual energy of India's holiest city.",
    "win-arguments.md": "Five psychological tricks to win any argument — from strategic confusion to the power of silence. Master the art of persuasion.",
    "yogic-breathing.md": "Introduction to Yogic Breathing (Pranayama) — techniques, step-by-step instructions, and the physical and mental benefits of breathwork.",
    "తరబల.md": "తారాబలం (Tara Balam) explained — how the strength of stars influences your birth nakshatra and its role in Vedic astrology.",
}

# ============================================================
# 2. POSTS TO DELETE
# ============================================================
POSTS_TO_DELETE = [
    "stop-overthinking.md",       # Empty post - only broken HTML fragments
    "law-of-life.md",             # Empty post - only broken HTML fragments
    "software-architecture-what-2016-07-22.md",  # Exact duplicate of software-architecture-what.md
]

# ============================================================
# 3. FIX FUNCTIONS
# ============================================================

def add_meta_description(content, description):
    """Add description to YAML frontmatter if not already present."""
    if "description:" in content.split("---")[1] if content.count("---") >= 2 else "":
        return content  # Already has description

    # Insert description after title line
    lines = content.split("\n")
    new_lines = []
    inserted = False
    for line in lines:
        new_lines.append(line)
        if not inserted and line.startswith("title:"):
            # Escape quotes in description
            desc_escaped = description.replace('"', '\\"')
            new_lines.append(f'description: "{desc_escaped}"')
            inserted = True

    if not inserted:
        # Fallback: insert after first ---
        new_lines = []
        found_first = False
        for line in lines:
            new_lines.append(line)
            if line.strip() == "---" and not found_first:
                found_first = True
            elif found_first and not inserted:
                desc_escaped = description.replace('"', '\\"')
                new_lines.insert(-1, f'description: "{desc_escaped}"')
                inserted = True

    return "\n".join(new_lines)


def fix_nested_figures(content):
    """
    Fix doubled <figure> wrapping pattern:
    <figure>
    <a href="URL" target="_blank">

    <figure>
    <a href="URL" target="_blank">
    <img ... />
    </a>
    </figure>

    </a>
    </figure>

    Should become just the inner figure.
    """
    # Pattern: outer figure+a wrapping inner figure+a+img
    pattern = (
        r'<figure>\s*'
        r'<a\s+href="[^"]*"\s+target="_blank">\s*'
        r'(<figure>\s*'
        r'<a\s+href="[^"]*"\s+target="_blank">\s*'
        r'<img[^>]*/>\s*'
        r'</a>\s*'
        r'</figure>)\s*'
        r'</a>\s*'
        r'</figure>'
    )

    fixed = re.sub(pattern, r'\1', content)
    return fixed


def fix_empty_alt_tags(content):
    """Fix images with empty alt tags - add descriptive alt text placeholder."""
    # Count replacements
    content = re.sub(r'alt=""', 'alt="Blog image"', content)
    return content


def count_fixes(original, fixed, name):
    """Count and report differences."""
    if original != fixed:
        orig_lines = set(original.split('\n'))
        fixed_lines = set(fixed.split('\n'))
        diff_count = len(orig_lines.symmetric_difference(fixed_lines))
        return True
    return False


# ============================================================
# 4. MAIN EXECUTION
# ============================================================

def main():
    if not os.path.isdir(POSTS_DIR):
        print(f"ERROR: Posts directory not found: {POSTS_DIR}")
        print("Make sure you're running this from the correct location.")
        return

    stats = {
        "deleted": 0,
        "descriptions_added": 0,
        "figures_fixed": 0,
        "alt_tags_fixed": 0,
        "total_modified": 0,
    }

    # Step 1: Delete empty/duplicate posts
    print("=" * 60)
    print("STEP 1: Removing empty and duplicate posts")
    print("=" * 60)
    for filename in POSTS_TO_DELETE:
        filepath = os.path.join(POSTS_DIR, filename)
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"  DELETED: {filename}")
            stats["deleted"] += 1
        else:
            print(f"  SKIP (not found): {filename}")

    # Step 2: Fix remaining posts
    print("\n" + "=" * 60)
    print("STEP 2: Fixing all remaining posts")
    print("=" * 60)

    for filename in sorted(os.listdir(POSTS_DIR)):
        if not filename.endswith(".md"):
            continue
        if filename in POSTS_TO_DELETE:
            continue

        filepath = os.path.join(POSTS_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            original = f.read()

        content = original

        # Fix 2a: Add meta description
        if filename in META_DESCRIPTIONS:
            before = content
            content = add_meta_description(content, META_DESCRIPTIONS[filename])
            if content != before:
                stats["descriptions_added"] += 1

        # Fix 2b: Fix nested <figure> tags
        before = content
        content = fix_nested_figures(content)
        if content != before:
            stats["figures_fixed"] += 1
            print(f"  FIXED nested figures: {filename}")

        # Fix 2c: Fix empty alt tags
        before = content
        content = fix_empty_alt_tags(content)
        if content != before:
            stats["alt_tags_fixed"] += 1

        # Write back if changed
        if content != original:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            stats["total_modified"] += 1
            print(f"  UPDATED: {filename}")

    # Step 3: Rename kuberneties files to kubernetes
    print("\n" + "=" * 60)
    print("STEP 3: Fixing 'kuberneties' typo in filenames")
    print("=" * 60)

    typo_files = [f for f in os.listdir(POSTS_DIR) if "kuberneties" in f]
    for old_name in typo_files:
        new_name = old_name.replace("kuberneties", "kubernetes")
        old_path = os.path.join(POSTS_DIR, old_name)
        new_path = os.path.join(POSTS_DIR, new_name)
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print(f"  RENAMED: {old_name} -> {new_name}")

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Posts deleted:          {stats['deleted']}")
    print(f"  Descriptions added:     {stats['descriptions_added']}")
    print(f"  Nested figures fixed:   {stats['figures_fixed']}")
    print(f"  Empty alt tags fixed:   {stats['alt_tags_fixed']}")
    print(f"  Total files modified:   {stats['total_modified']}")
    print(f"  Files renamed:          {len(typo_files)}")
    print("\nDone! Run 'hugo server' to preview changes.")


if __name__ == "__main__":
    main()
