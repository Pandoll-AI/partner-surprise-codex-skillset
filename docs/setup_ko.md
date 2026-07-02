# 설치 및 사용 가이드

## 1. 압축 해제

```bash
unzip partner-surprise-codex-skillset.zip
cd partner-surprise-codex-skillset
```

## 2. 개인 데이터 파일 만들기

예시 파일을 복사해서 실제 값으로 바꾸거나, `$partner-profile-maintainer`로 12문항 취향 인터뷰를 먼저 진행하세요.

```bash
cp data/partner_profile.example.json data/partner_profile.json
cp data/anniversaries.example.json data/anniversaries.json
cp data/constraints.example.json data/constraints.json
cp data/candidates.example.json data/candidates.json
```

`partner_profile.json`이 없거나 예시 그대로라면 추천 전에 인터뷰를 먼저 진행합니다.

`anniversaries.json`의 `MM-DD`는 실제 생일, 기념일 등으로 바꿔야 합니다.

## 3. Codex 스킬로 설치

전역 개인 스킬:

```bash
./install.sh global
```

특정 프로젝트용:

```bash
./install.sh project
```

## 4. 확인

```bash
python3 scripts/demo_run.py
```

## 5. Codex에서 호출

```text
$surprise-orchestrator
이번 주말에 파트너에게 작은 서프라이즈를 준비하고 싶어. data 폴더를 읽고 추천해줘.
```

```text
$partner-profile-maintainer
data/partner_profile.json이 아직 없어. 12문항 인터뷰로 프로필 초안을 만들어줘.
```

## 6. 자동화

Codex App Automations를 사용할 수 있다면 `automations/*.prompt.md` 파일 내용을 붙여 넣고 주기만 설정하면 됩니다.

추천 주기:

- daily trigger radar: 매일 아침
- weekly surprise scan: 주 1회
- monthly trend watch: 월 1회
- pre anniversary: 매일 또는 주 2회
