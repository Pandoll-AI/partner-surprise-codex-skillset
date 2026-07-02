# Partner Preference Interview

Use this interview when `data/partner_profile.json` is missing, empty, or still looks like the example file.

Ask 12 questions in 2-3 batches. Tell the user they can skip any question. Convert answers into `data/partner_profile.json` using only information that helps low-pressure surprise planning.

## Batch 1: Taste and Atmosphere

1. 파트너가 편하게 좋아하는 음식, 디저트, 음료는 무엇인가요?
2. 피해야 할 음식, 알레르기, 향, 소재, 장소 유형이 있나요?
3. 파트너가 좋아하는 분위기는 어떤 쪽인가요? 예: 조용함, 활기참, 고급스러움, 캐주얼함, 자연, 전시, 공연.
4. 공개적인 이벤트와 조용한 1:1 이벤트 중 어느 쪽을 더 편하게 느끼나요?

## Batch 2: Gifts and Experiences

5. 최근 파트너가 좋아했다고 말한 선물, 장소, 경험이 있나요?
6. 반대로 부담스러워했거나 별로 좋아하지 않았던 선물, 장소, 이벤트 방식이 있나요?
7. 선물은 실용적인 것, 감성적인 것, 경험형 중 어느 쪽이 더 잘 맞나요?
8. 꽃, 손편지, 디저트, 작은 집안일/심부름 같은 가벼운 배려 중 잘 맞을 만한 것은 무엇인가요?

## Batch 3: Timing and Constraints

9. 평일 저녁, 주말 낮, 주말 저녁 중 어떤 시간이 가장 부담이 적나요?
10. 이동 시간, 예산, 예약/취소 가능성에서 지켜야 할 선이 있나요?
11. 챙기면 좋은 기념일이나 계절 이벤트가 있나요? 날짜는 `MM-DD` 또는 `YYYY-MM-DD`로 받을 수 있습니다.
12. 다음 서프라이즈가 어떤 느낌이면 좋겠나요? 예: 회복, 감사, 데이트, 휴식, 장난스러움, 기념.

## Mapping Rules

- Put foods, styles, activities, brands, and preferred atmospheres into `preferences.likes` or `preferences.style_tags`.
- Put allergies, dietary restrictions, public-attention avoidance, and hard dislikes into `preferences.dislikes` or `preferences.allergies_or_hard_constraints`.
- Put date-like answers into `data/anniversaries.json` only when the user provides a date.
- Put budget, travel time, schedule, childcare, and cancellation constraints into `data/constraints.json`.
- Put recent reactions into `history` only when they are useful for future recommendations.
- Mark direct statements as `confidence: high` when adding structured notes.
