from django.db import models
from django.contrib.auth.models import User

# 과학 이슈 모델
class ScienceIssue(models.Model):
    title = models.CharField(max_length=200)  # 제목
    content = models.TextField()  # 내용
    category = models.CharField(max_length=100)  # 카테고리
    views = models.PositiveIntegerField(default=0)  # 조회수
    created_at = models.DateTimeField(auto_now_add=True)  # 생성일
    updated_at = models.DateTimeField(auto_now=True)  # 수정일

    def __str__(self):
        return self.title


# 댓글 모델
class Comment(models.Model):
    issue = models.ForeignKey(ScienceIssue, on_delete=models.CASCADE, related_name='comments')  # 과학 이슈 참조
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 작성자
    content = models.TextField()  # 댓글 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 생성일

    def __str__(self):
        return f"Comment by {self.author} on {self.issue}"


# 위키 협업 도구 모델
class WikiCollaboration(models.Model):
    title = models.CharField(max_length=200)  # 위키 제목
    content = models.TextField()  # 위키 내용
    contributors = models.ManyToManyField(User, related_name='wiki_contributions')  # 기여자
    created_at = models.DateTimeField(auto_now_add=True)  # 생성일
    updated_at = models.DateTimeField(auto_now=True)  # 수정일

    def __str__(self):
        return self.title


# Q&A 게시판 모델
class Question(models.Model):
    title = models.CharField(max_length=200)  # 질문 제목
    content = models.TextField()  # 질문 내용
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 작성자
    created_at = models.DateTimeField(auto_now_add=True)  # 생성일

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')  # 질문 참조
    content = models.TextField()  # 답변 내용
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 작성자
    created_at = models.DateTimeField(auto_now_add=True)  # 생성일

    def __str__(self):
        return f"Answer to {self.question}"


# 뉴스/이론 게시판 모델
class NewsTheoryPost(models.Model):
    title = models.CharField(max_length=200)  # 게시글 제목
    content = models.TextField()  # 게시글 내용
    category = models.CharField(max_length=100)  # 카테고리 (뉴스, 이론 등)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 작성자
    created_at = models.DateTimeField(auto_now_add=True)  # 생성일

    def __str__(self):
        return self.title
