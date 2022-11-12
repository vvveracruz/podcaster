init:
	pipenv install --dev
	brew bundle install --file ./../Brewfile

init-android:
	pipenv install --dev
	brew bundle install --file ./../Brewfile
	pipenv run briefcase create android
	
dev-run:
	pipenv install --dev
	pipenv run briefcase dev

macos-run:
	pipenv run briefcase update -d
	pipenv run briefcase build
	pipenv run briefcase run

android-run:
	pipenv run briefcase update android -d
	pipenv run briefcase build android
	pipenv run briefcase run android -d @beePhone

## dev utils

clean:
	rm *.log

lint: 
	pipenv run black src/

