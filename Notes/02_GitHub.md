# Git 두 번째

1. 빈 폴더 추가 시, 변경사항은 status에 나타나지 않는다.

2. 일반적으로 .gitkeep이라고 하는 파일을 생성한다.

   ```bash
   $ touch .gitkeep
   ```

3. 그러면 빈 폴더도 커밋할 수 있다.



# GitHub 원격저장소 활용

1. 원격 저장소 정보를 로컬 저장소에 추가 (한 번만)

   → git에게 원격 저장소(url)를 origin이라는 이름으로 추가해달라는 요청

   ```bash
   $ git remote add origin https://github.com/jupiter6676/kdt_test.git
   ```

2. 원격 저장소의 정보 확인

   ```bash
   $ git remote -v
   ```

3. `push` (add, commit한 후 마지막으로)

   ```bash
   $ git push origin master
   ```

   ✨ 로컬 폴더의 파일, 폴더가 아닌 버전(커밋)이 올라간다.

   
   
   ✔️ 나는 이거 하니까 error: failed to push some refs to 에러, 'origin' does not appear to be a git repository 에러가 났었는데, 처음에 Repository 만들 때 README.md 추가하기 옵션 클릭해서 그렇더라.. 아예 저장소 삭제하고 처음부터 만드니까 됐음. 선생님 말씀을 잘 듣자..!!!
   
   ✔️ 후에도 failed to push some refs to 에러가 뜬다면: 원격 저장소 커밋 ≠ 로컬 저장소 커밋 → 원격 저장소의 변경 사항을 가져와야 함.
   
   ```bash
   $ git pull origin master
   ```
   
   를 하면 또 Merge branch 'master ' of (URL) 어쩌구 뜨면서 vi 편집기가 나올 수 있음.
   
   ```bash
   $ git config --global core.editer "code --wait"
   ```
   
   그럼 이걸 치면 다시 push가 돼. 그리고 커밋을 보면, Merge가 되었다는 일종의 메시지를 볼 수 있다.
   
4. 협업할 땐 반드시 먼저 pull 받고 로컬에서 작업해야 함. 안 그러면 Conflict 발생하니깐..



# .gitignore

1. 버전관리를 하지 않는 파일/폴더 이름을 .gitignore 파일에 적으면, git status에 표시되지 X
2. 이미 커밋된 파일은 삭제 후 진행
3. 아래의 사이트에서, `.gitignore` 템플릿을 가져올 수 O
   - [gitignore.io](https://www.toptal.com/developers/gitignore/)
   - [A collection of `.gitignore` templates](https://github.com/github/gitignore)



# 실습

- TIL 각자 원하는 형식으로 정리
  - 2일간 배웠던 내용도 정리
  - TIL 주소를 Syllaverse에 제출
- 선택 과제
  - GitHub 프로필 README