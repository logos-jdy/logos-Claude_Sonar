# 통합 연동 실습용 예제

이 저장소는 **SW QA 교육용 실습 자료**입니다.

일부 코드 품질 문제를 의도적으로 포함한 Python 예제 파일을 제공합니다. 실습에서는 GitHub에 예제 파일을 등록하고, Jenkins와 SonarQube로 정적분석한 뒤, Claude Code를 이용해 이슈를 확인하고 코드를 수정하여 GitHub에 반영합니다.

## 파일 구성

| 파일 | 용도 |
| --- | --- |
| `src/order_service.py` | SonarQube 정적분석 대상인 예제 소스코드 |
| `sonar-project.properties` | SonarQube 분석용 프로젝트 정보 |
| `.gitignore` | GitHub에 올리지 않을 임시 파일 지정 |

## 실습 흐름

1. 예제 파일을 GitHub 저장소에 등록합니다.
2. Jenkins에서 정적분석을 실행하고 SonarQube의 이슈를 확인합니다.
3. Claude Code에서 SonarQube 이슈와 예제 소스코드를 불러옵니다.
4. Claude Code에 이슈 분석 및 코드 수정을 요청합니다.
5. 수정 내용을 확인한 후 Claude Code를 통해 GitHub에 커밋·푸시합니다.
6. Jenkins에서 다시 분석을 실행해 SonarQube 이슈가 개선되었는지 확인합니다.

> 이 저장소는 실습용 예제입니다. 코드를 직접 작성하거나 Python 단위 테스트를 수행하는 개발 실습은 포함하지 않습니다. 세부 조작 방법은 별도 실습 매뉴얼을 참고하세요.

**참고:** SonarQube의 검출 이슈와 건수는 버전 및 품질 프로파일에 따라 달라질 수 있습니다.
