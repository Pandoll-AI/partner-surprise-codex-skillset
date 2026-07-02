# Partner Surprise Codex Skillset

![Partner Surprise Codex Skillset hero](assets/hero.png)

파트너에게 자연스럽고 의미 있는 서프라이즈를 제안하기 위한 Codex Skills 세트입니다.

이 패키지는 다음을 목표로 합니다.

- 기념일, 한국식 시즌 이벤트, 가족/감정 신호를 트리거로 감지
- 선물, 식당, 여행, 작은 배려 액션을 최신 트렌드와 개인 맥락으로 검토
- “왜 지금 이걸 하는지”가 자연스럽게 설명되는 서프라이즈 플랜 생성
- 과도한 감시, 조작, 허위 이유 만들기를 피하고 관계 회복과 배려 중심으로 제안

## 포함 구성

```text
.agents/skills/                     Codex Skill folders
  surprise-orchestrator/             전체 플랜을 조율하는 메인 스킬
  life-event-trigger-radar/          기념일/감정/일정 트리거 스캔
  trend-research-scout/              트렌드·근거·검색 질 관리
  gift-idea-selector/                선물 후보 생성·스코어링
  restaurant-date-planner/           식당/데이트 코스 제안
  travel-getaway-planner/            여행/호텔/휴식 제안
  relationship-message-writer/       카드/메시지/말투 작성
  partner-profile-maintainer/        파트너 취향 프로필 관리와 12문항 인터뷰
.codex/agents/                       선택용 Codex helper profiles
data/                                개인화 입력 예시 JSON
scripts/                             로컬 데모/브리프 생성 스크립트
automations/                         Codex App Automations에 붙여 넣을 프롬프트
```

## 설치 방법

### 전역 개인 스킬로 설치

```bash
cd partner-surprise-codex-skillset
./install.sh global
```

설치 후 Codex CLI/앱을 재시작하면 `$HOME/.agents/skills` 아래의 스킬을 감지합니다.

### 특정 프로젝트에만 사용

현재 폴더 자체가 repo 안이라면 `.agents/skills`를 그대로 두고 Codex를 그 repo에서 실행하면 됩니다.

## 빠른 실행 예시

프로필이 없거나 예시 파일만 있는 경우 `$partner-profile-maintainer`가 먼저 12문항 취향 인터뷰를 진행합니다. 인터뷰는 좋아하는 분위기, 피해야 할 것, 선물/경험 선호, 예산과 일정 부담을 짧게 묻고 필요한 필드만 저장합니다.

```bash
python3 scripts/demo_run.py
python3 scripts/generate_surprise_brief.py \
  --profile data/partner_profile.example.json \
  --anniversaries data/anniversaries.example.json \
  --constraints data/constraints.example.json \
  --candidates data/candidates.example.json \
  --date 2026-07-02
```

## Codex에서 쓰는 예시 프롬프트

```text
$surprise-orchestrator
이번 주말에 파트너에게 부담스럽지 않은 서프라이즈를 하나 준비하고 싶다.
내 data/ 폴더의 프로필과 제약을 읽고, 최신 트렌드 근거가 붙은 식당/선물/경험 후보를 비교한 뒤 실행 플랜을 만들어줘.
```

```text
$partner-profile-maintainer
아직 data/partner_profile.json이 없어. 먼저 파트너 취향 인터뷰를 진행하고 프로필 초안을 만들어줘.
```

```text
$life-event-trigger-radar
앞으로 45일 안에 챙길 만한 기념일, 한국식 이벤트, 감정 케어 트리거를 스캔해줘.
```

## 중요한 원칙

- 최신 트렌드, 가격, 예약 가능 여부는 반드시 실행 시점에 재확인해야 합니다.
- 트렌드 근거가 필요하면 웹 브라우징이나 검색 MCP가 필요합니다. 사용할 수 없으면 검색 쿼리와 검증 체크리스트만 생성하고 사실처럼 쓰지 않습니다.
- 거짓말을 만들어내기보다 “자연스러운 이유”와 “진심 어린 설명”을 우선합니다.
- 파트너의 사적 메시지, 위치, 감정 상태를 동의 없이 감시하도록 설계하지 않습니다.
- 프로필에는 서프라이즈 실행에 필요한 취향과 제약만 저장합니다.
