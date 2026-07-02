.PHONY: demo brief install-global install-project

demo:
	python3 scripts/demo_run.py

brief:
	python3 scripts/generate_surprise_brief.py --profile data/partner_profile.example.json --anniversaries data/anniversaries.example.json --constraints data/constraints.example.json --candidates data/candidates.example.json

install-global:
	./install.sh global

install-project:
	./install.sh project
