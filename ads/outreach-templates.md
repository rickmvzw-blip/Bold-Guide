# Bold Guide LLC — Week 1 Distribution Outreach Templates

Goal: get the first 3 honest customer reviews. Give product away, ask for
2 sentences in 7 days. Plain prose, no marketing voice.

Attachments to keep handy:
- ADHD sampler PDF: `ads/adhd-5-free-prompts-sampler.pdf`
- Live page (LeadForge): https://boldguide.io/leadforge/
- Live page (ADHD): https://boldguide.io/adhd150prompts/
- Live page (Bold Presence): https://boldguide.io/web-design/

To mint a free deliverable for a recipient (server must be live):

```bash
# LeadForge API key (free)
curl -X POST "https://leadforge-rh03.onrender.com/admin/grant?token=$ADMIN_TOKEN&product=leadforge&email=alice@example.com"

# ADHD 150-prompt download (free)
curl -X POST "https://leadforge-rh03.onrender.com/admin/grant?token=$ADMIN_TOKEN&product=adhd&email=alice@example.com"
```

Email is auto-sent. Save the JSON response (contains the key/URL) in case the
recipient's spam filter eats the email.

---

## A. ADHD Brain Unlock — to a friend / coach / parent

**Subject:** A free thing I built — and a small ask

Hi [Name],

I built a 150-prompt AI pack for people with ADHD (mornings, focus,
overwhelm, planning). Before I push it anywhere, I'd love an honest
gut-check from someone whose opinion I trust.

Attached is a free 5-prompt sample. If you find it useful, I can grant you
the full 150-pack for free (no payment, no card) — I just ask that you
send me **two honest sentences** about it within 7 days. Even "this is
mid, here's why" is more useful than silence.

If it's not for you, please pass it to one person you think it might help.

Thanks for being on the short list.

Ricardo
boldguide.io · ricardo@boldguide.io

---

## B. LeadForge — to a sales-ops / agency / indie-hacker contact

**Subject:** Free lifetime LeadForge key — 2-sentence review in return?

Hi [Name],

I shipped a B2B lead-enrichment API ($97 one-time, lifetime access). Before
I run ads at it, I want it tested by 3 people who actually do outbound or
agency work. You're one of them.

I'll set you up with a free lifetime key (no card, no expiry) if you can
do two things:
1. Try it on a handful of leads this week — Swagger docs at
   https://leadforge-rh03.onrender.com/docs.
2. Send me **two honest sentences** by [date 7 days out]: what worked,
   what didn't. Whatever you say goes — I'd rather hear "data quality is
   weak on X" than nothing.

If you're game, reply with the email you want the key sent to.

Thanks,
Ricardo
boldguide.io/leadforge/

---

## C. Bold Presence — to a small-business owner who needs a site

**Subject:** Quick question about your website

Hi [Name],

I just launched a freelance web-build service under my LLC — full
4-week build for $997, or à-la-carte from $169.99. Bilingual (EN/ES).

I'm offering the first 3 clients a $200 credit in exchange for letting me
use the finished site as a portfolio piece + a short written testimonial
when it's live. No tricks — your site, your domain, your content.

If you (or someone you know) is sitting on a "we really need a real
website" problem, I'd love a 15-minute call this week.

Page: https://boldguide.io/web-design/
Direct: (951) 544-9913 · ricardo@boldguide.io

Ricardo
Bold Guide LLC

---

## D. DM-length variant (LinkedIn / Reddit / Slack)

Quick ask: I built [LeadForge / a 150-prompt ADHD pack / a web-build
service]. Free for the first 3 reviewers — I just want 2 honest
sentences back in 7 days. Up for it? I'll send the link.

---

## Follow-up at day 7

**Subject:** Quick nudge — 2 sentences?

Hi [Name],

Following up on the [LeadForge key / ADHD pack / web build] from last
week. No worries if you didn't get to it — totally fine to say so. If
you did try it, even one sentence helps me decide what to fix next.

Thanks either way.
Ricardo

---

## Tracking

Keep a simple list (Notion, Sheets, plain markdown — doesn't matter):

| Date sent | Name | Product | Email | Granted? | Reply by | Got review? |
|-----------|------|---------|-------|----------|----------|-------------|

Target: 3 reviews per product by end of Week 1. Pause new outreach when
you hit 5 outstanding per product so you don't get swamped chasing
follow-ups.
