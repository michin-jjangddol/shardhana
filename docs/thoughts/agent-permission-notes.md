Location: `docs/thoughts/agent-permission-notes.md`

# Agent Permissions
*(Not what AI can do — but what it must not be allowed to do.)*  

*(Shardhana Thought Archive)*
*Date: 2026-07-11*

<p align="center">
  <img src="../assets/images/agent-permission-notes-en.png" width="90%">
</p>

---

## 1. A Question That Started with a NAS

It started as a story about a NAS.

I realized I hadn't been using Synology Drive properly, and that led naturally into a conversation about user permissions and project permissions.

Then, out of nowhere, one question surfaced.

> What permissions should an AI agent actually work with?

This wasn't just a Cursor problem, or a Claude problem.

It felt like something every environment working alongside AI would eventually have to face.

---

## 2. A Question I've Had for a Long Time

This wasn't a new thought.

Twenty-seven years ago, the first time I installed Linux,

I ran into the concepts of

User,

Group,

Permission.

And ever since, one thing has bothered me.

Why do so many companies

not divide permissions by project,

and instead let everyone

read,

edit,

and delete

every folder?

For more than twenty years,

that has always felt a little off to me.

---

## 3. Least Privilege — An Obvious Principle

IT has had a principle called

"Least Privilege"

for a very long time.

Grant only what's needed.

Withhold everything else.

For example,

the person responsible for Project A

should only be able to edit Project A.

Project B should be read-only to them,

or invisible entirely.

This isn't a special technique.

It's a basic, time-tested piece of system design.

---

## 4. So Why Is AI Different?

Traditional software

only did what a person told it to do.

So as long as permissions were set correctly,

the program never went beyond its boundary.

AI agents are different.

Give one a goal,

and it figures out the path there on its own.

Which means

it can choose actions no one anticipated,

simply because that's what solving the problem seemed to require.

That, to me, is the real difference from ordinary software.

---

## 5. A Prompt Is a Promise. A Permission Is an Enforcement.

Suppose you tell an AI:

> Only read the docs folder — don't write to it.

That's not a permission.

It's just a request for a certain behavior.

If the AI misunderstands,

misjudges,

or hits an edge case,

there's no way to fully rule out the chance it breaks that rule on its own.

A prompt is a promise.

A permission is an enforcement.

The two are not the same thing at all.

---

## 6. The Operating System Already Had the Answer

Thinking it through, this turned out not to be a new problem.

Windows,

and Linux,

have both offered

users,

groups,

ACLs,

and read, write, execute, and delete permissions

for decades.

Rather than inventing a new permission system just for AI,

letting AI operate inside the permission system an OS already provides

looked like the simplest and safest path available.

---

## 7. AI as Just Another User

What if AI were treated as another user account?

Shana could hold an account that can only edit documents.

Laude could hold one that can only edit source code.

Gemi could hold one that's read-only.

Under that setup,

AI can't step outside what the OS allows.

Permission denied.

The final call isn't made by the AI.

It's made by the operating system.

---

## 8. The Current Reality of AI IDEs

But today's AI IDEs seem to be heading in a different direction.

Most of them

simply inherit whatever permissions the logged-in user already has.

Which means

the AI gets everything I have.

If I can edit a document, the AI can edit it.

If I can delete a file, the AI can delete it.

If I can push to Git, the AI can push too.

That was a bit of a surprise.

---

## 9. Which Is Why People Split Repositories Instead

So many developers today

separate repositories instead of separating permissions.

A docs repository.

A source repository.

An experiments repository.

The AI only sees whatever repository it's been pointed at.

This can be safe enough, in practice.

But it feels less like a real solution

and more like a workaround for what current tools can't yet do properly.

---

## 10. Least Privilege for the Age of AI

AI makes judgment calls the way a person does.

Which may mean it needs even tighter permission controls than a person would.

What matters isn't whether the AI ever makes a mistake.

It's whether the system limits the blast radius when it does.

That's the exact role

an operating system has quietly played for decades.

---

## 11. Coming Back to Where I Started

At first, I assumed AI would need an entirely new permission system of its own.

But following the thought all the way through,

the answer turned out to already exist —

it had been sitting inside the operating system the whole time.

What AI needs isn't a new permission system.

It's respect for the one that already exists.

Not new rules,

but working within a system that's already been proven.

---

## 12. Hidden Nothing

Within Shardhana,

AI isn't meant to be treated as something special.

Both people and AI

should operate inside the same system,

follow the same rules,

and use the same permission structure.

Who did what, with which permissions,

what got changed,

and what got read —

all of it should stay as visible as possible.

Hidden nothing.

AI doesn't get an exception either.

---

## 13. An Old Idea, Rediscovered in the Age of AI

Maybe it took the arrival of AI

for the concept I first met in Linux, twenty-seven years ago —

users and permissions —

to become one of the most important questions again.

A new era doesn't always call for new technology.

Sometimes,

a principle that's already been proven

turns out to be the most forward-looking answer of all.

---

This document was prepared with the assistance of Shana (GPT) and Laude (Claude).

---
<br>
<br>

# 에이전트 권한
*(AI는 무엇을 할 수 있는가보다, 무엇을 할 수 없어야 하는가.)*  

*(Shardhana Thought Archive)*
*Date: 2026-07-11*

<p align="center">
  <img src="../assets/images/agent-permission-notes-ko.png" width="90%">
</p>

---

## 1. NAS에서 시작된 의문

처음에는 NAS 이야기였다.

Synology Drive를 제대로 사용하지 않았다는 사실을 알게 되었고,
사용자 권한과 프로젝트 권한에 대한 이야기가 자연스럽게 이어졌다.

그러다 문득 하나의 질문이 떠올랐다.

> AI 에이전트는 과연 어떤 권한으로 일해야 하는가?

이 질문은 단순히 Cursor나 Claude만의 문제가 아니었다.

앞으로 AI와 함께 일하는 모든 환경에서 반드시 고민해야 할 문제처럼 느껴졌다.

---

## 2. 오래전부터 가지고 있던 의문

사실 이 생각은 오늘 처음 생긴 것이 아니다.

27년 전 리눅스를 처음 설치했을 때,

사용자(User),
그룹(Group),
권한(Permission)

이라는 개념을 처음 접했다.

그때부터 항상 의문이었다.

왜 많은 회사들은

프로젝트마다 권한을 나누지 않고,

모든 사람이

모든 폴더를

읽고,
수정하고,
삭제할 수 있도록 운영하는 걸까.

20년이 넘도록

항상 조금 이상하다는 생각을 가지고 있었다.

---

## 3. 최소 권한이라는 너무나 당연한 원칙

IT에서는 오래전부터

'최소 권한(Least Privilege)'

이라는 원칙을 사용해 왔다.

필요한 권한만 부여한다.

필요 없는 권한은 주지 않는다.

예를 들어

프로젝트 A 담당자는

프로젝트 A만 수정할 수 있고,

프로젝트 B는

읽기만 가능하거나

아예 접근하지 못해야 한다.

이것은 특별한 기술이 아니라,

오랫동안 검증된 시스템 설계의 기본이다.

---

## 4. 그런데 AI는 왜 다른가

기존 프로그램은

사람이 시키는 일만 수행했다.

그래서

권한만 올바르게 설정하면

프로그램은 그 범위를 벗어나지 않았다.

하지만 AI 에이전트는 다르다.

목표를 주면

스스로 해결 방법을 찾는다.

그래서

문제를 해결하기 위해

예상하지 못한 행동을 선택할 수도 있다.

바로 이 지점이

기존 프로그램과 가장 큰 차이라고 느껴졌다.

---

## 5. 프롬프트는 약속이다. 권한은 강제다.

예를 들어

AI에게

> docs 폴더는 읽기만 해.

라고 지시했다고 하자.

이것은

권한이 아니다.

단지

행동을 요청한 것이다.

AI가

착각하거나,

판단을 잘못하거나,

예외 상황을 만나면

그 규칙을 스스로 어길 가능성을 완전히 없앨 수는 없다.

프롬프트는 약속이다.

권한은 강제다.

둘은 전혀 다르다.

---

## 6. 운영체제는 이미 답을 가지고 있었다

생각해 보니

이 문제는 새로운 문제가 아니었다.

Windows도,

Linux도,

이미

사용자,

그룹,

ACL,

읽기,

쓰기,

실행,

삭제

권한을 수십 년 전부터 제공하고 있었다.

AI만을 위한 새로운 권한 체계를 만드는 것이 아니라,

이미 검증된 운영체제의 권한 안에서

AI가 일하도록 만드는 것이

가장 단순하면서도 가장 안전한 방법처럼 보였다.

---

## 7. AI는 또 하나의 사용자

만약

AI를

또 하나의 사용자 계정으로 생각한다면 어떨까.

예를 들어

Shana는

문서만 수정할 수 있고,

Laude는

소스만 수정할 수 있으며,

Gemi는

읽기만 가능한 계정을 사용한다.

그러면

AI는

운영체제가 허용한 범위 밖으로

나갈 수 없다.

Permission Denied.

최종 판단은

AI가 아니라

운영체제가 내린다.

---

## 8. 현재 AI IDE의 현실

하지만 현재의 AI IDE는

조금 다른 방향으로 발전하고 있는 것처럼 보인다.

대부분은

현재 로그인한 사용자의 권한을 그대로 사용한다.

즉,

AI는

내가 가진 권한을 그대로 물려받는다.

문서를 수정할 수 있으면

AI도 수정한다.

파일을 삭제할 수 있으면

AI도 삭제한다.

Git Push가 가능하면

AI도 Push를 수행한다.

조금은 의외였다.

---

## 9. 그래서 저장소를 분리한다

현재 많은 개발자들은

권한 대신

저장소를 분리한다.

문서 저장소,

소스 저장소,

실험 저장소.

AI는

열어준 저장소만 본다.

이 방법도 충분히 안전할 수 있다.

하지만

근본적인 해결책이라기보다는,

현재 도구의 한계를

운영 방식으로 보완하는 느낌이 들었다.

---

## 10. AI 시대의 최소 권한

AI는

사람처럼 판단한다.

그래서

사람보다 더 강한 권한 통제가 필요할 수도 있다.

중요한 것은

AI가 실수하지 않는 것이 아니다.

실수하더라도

피해 범위를 시스템이 제한하는 것이다.

그것이

수십 년 동안

운영체제가 맡아온 역할이다.

---

## 11. 다시 처음으로 돌아오다

처음에는

AI만을 위한 새로운 권한 체계가 필요할 것이라고 생각했다.

하지만 끝까지 생각을 따라가 보니,

결국 답은

이미 오래전부터

운영체제 안에 존재하고 있었다.

AI에게 필요한 것은

새로운 권한 시스템이 아니다.

기존의 권한 시스템을

존중하는 것이다.

새로운 규칙을 만드는 것이 아니라,

이미 검증된 시스템 안에서

함께 일하는 것이다.

---

## 12. Hidden Nothing

Shardhana에서는

AI를 특별한 존재로 만들고 싶지 않다.

사람과 AI 모두

같은 시스템 안에서,

같은 규칙을 따르고,

같은 권한 체계를 사용해야 한다.

누가 어떤 권한으로 작업했는지,

무엇을 수정했고,

무엇을 읽었는지,

모든 과정은 가능한 한 투명해야 한다.

Hidden Nothing.

AI도

예외가 되어서는 안 된다.

---

## 13. AI 시대에 다시 만난 오래된 기술

어쩌면

AI 시대가 되어서야

27년 전 리눅스에서 처음 만났던

사용자와 권한이라는 개념이

다시 가장 중요한 주제로 돌아오고 있는 것인지도 모르겠다.

새로운 시대는

항상 새로운 기술만 요구하는 것은 아니다.

때로는

오랫동안 검증된 원칙이

가장 미래적인 답이 되기도 한다.

---

이 문서는 샤나(GPT)와 로드(Claude)의 도움으로 작성되었습니다.
