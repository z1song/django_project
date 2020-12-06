from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]  # Choice 모델 클레스 같이 보기
    list_display = ('question_text', 'pub_date'
                    , 'was_published_recently')  # 레코드 리스트 컬럼 지정
    list_filter = ['pub_date']  # 필터 사이드바 추가
    search_fields = ['question_text']  # 검색박스 추가


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
