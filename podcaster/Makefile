init:
	pipenv install --dev
	brew bundle install --file ./../Brewfile

init-android:
	pipenv install --dev
	brew bundle install --file ./../Brewfile
	pipenv run briefcase create android
	
dev-run:
	pipenv run briefcase dev

lint: 
	pipenv run black src/

build:
	pipenv run briefcase update
	pipenv run briefcase build

package:
	pipenv run briefcase build
	pipenv run briefcase package --no-sign

run:
	pipenv run briefcase --update run

android-run:
	pipenv run briefcase --update run android

clean:
	rm *.log

