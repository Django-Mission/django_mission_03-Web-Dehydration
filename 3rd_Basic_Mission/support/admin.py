from django.contrib import admin
from .models import Faq, Inquiry, Answer

# Register your models here.

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0
    min_num = 3
    max_num = 5
    verbose_name = '답변'
    verbose_name_plural = '답변'

# Register your models here.

@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'updated_at')
    list_filter = ('category', )
    search_fields = ('question',)
    search_help_text = '질문 검색이 가능합니다.'

@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'creator', 'status')
    list_filter = ('category', 'status')
    search_fields = ('title', 'telephone', 'creator__username' ,'creator__email')
    search_help_text = '제목, 이메일, 전화번호 검색이 가능합니다.'
    inlines = [AnswerInline]

    actions = ['make_published']

    def make_published(modeladmin, request, queryset):
        for item in queryset:
            if item.reply_via_email == True:
                print(item.email)
            else:
                pass

            if item.reply_via_MMS == True:
                print(item.telephone)
            else:
                pass