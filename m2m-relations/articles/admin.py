from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()
        main_tags_count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_tags_count += 1
            if main_tags_count > 1:
                raise ValidationError('Только один тег может быть основным.')


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass