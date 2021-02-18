# Generated by Django 3.0.8 on 2021-02-16 16:19

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtailstreamforms.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_comments_xtd', '0006_auto_20181204_0948'),
        ('wagtailtrans', '0009_create_initial_language'),
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailstreamforms', '0002_form_site'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleIndexPage',
            fields=[
                ('translatablepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailtrans.TranslatablePage')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailtrans.translatablepage',),
        ),
        migrations.CreateModel(
            name='ArticlePage',
            fields=[
                ('translatablepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailtrans.TranslatablePage')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
                ('featured', models.BooleanField(default=False)),
                ('body', wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'image', 'code', 'blockquote'])), ('code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.core.blocks.TextBlock(identifier='code', label='Code'))], label='Code')), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('caption', wagtail.core.blocks.CharBlock(label='Caption', required=False)), ('float', wagtail.core.blocks.ChoiceBlock(choices=[('right', 'Right'), ('left', 'Left'), ('center', 'Center')], label='Float', required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], label='Size', required=False))])), ('video', wagtail.core.blocks.StructBlock([('video', wagtail.embeds.blocks.EmbedBlock(label='Video')), ('caption', wagtail.core.blocks.CharBlock(label='Caption', required=False)), ('float', wagtail.core.blocks.ChoiceBlock(choices=[('right', 'Right'), ('left', 'Left'), ('center', 'Center')], label='Float', required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], label='Size', required=False))]))])),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailtrans.translatablepage',),
        ),
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('translatablepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailtrans.TranslatablePage')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
                ('body', wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('form', wagtail.core.blocks.StructBlock([('form', wagtailstreamforms.blocks.FormChooserBlock()), ('form_action', wagtail.core.blocks.CharBlock(help_text='The form post action. "" or "." for the current page or a url', required=False)), ('form_reference', wagtailstreamforms.blocks.InfoBlock(help_text='This form will be given a unique reference once saved', required=False))]))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailtrans.translatablepage',),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('title_en', models.CharField(max_length=50, null=True)),
                ('title_fr', models.CharField(max_length=50, null=True)),
                ('title_nl', models.CharField(max_length=50, null=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, help_text='Unique identifier of menu. Will be populated automatically from title of menu. Change only if needed.', populate_from='title')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TextPage',
            fields=[
                ('translatablepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailtrans.TranslatablePage')),
                ('text', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailtrans.translatablepage',),
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('name_en', models.CharField(max_length=255, null=True)),
                ('name_fr', models.CharField(max_length=255, null=True)),
                ('name_nl', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ThemeIndexPage',
            fields=[
                ('translatablepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailtrans.TranslatablePage')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailtrans.translatablepage',),
        ),
        migrations.CreateModel(
            name='ThemePage',
            fields=[
                ('translatablepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailtrans.TranslatablePage')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
                ('caption', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('theme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='themepages', to='cms.Theme')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailtrans.translatablepage',),
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(help_text='Title of menu item that will be displayed', max_length=50)),
                ('title_en', models.CharField(help_text='Title of menu item that will be displayed', max_length=50, null=True)),
                ('title_fr', models.CharField(help_text='Title of menu item that will be displayed', max_length=50, null=True)),
                ('title_nl', models.CharField(help_text='Title of menu item that will be displayed', max_length=50, null=True)),
                ('link_url', models.CharField(blank=True, help_text='URL to link to, e.g. /accounts/signup (no language prefix, LEAVE BLANK if you want to link to a page instead of a URL)', max_length=500, null=True)),
                ('title_of_submenu', models.CharField(blank=True, help_text='Title of submenu (LEAVE BLANK if there is no custom submenu)', max_length=50, null=True)),
                ('show_when', models.CharField(choices=[('always', 'Always'), ('logged_in', 'When logged in'), ('not_logged_in', 'When not logged in')], default='always', max_length=15)),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('link_page', models.ForeignKey(blank=True, help_text='Page to link to (LEAVE BLANK if you want to link to a URL instead)', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailtrans.TranslatablePage')),
                ('menu', modelcluster.fields.ParentalKey(help_text='Menu to which this item belongs', on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='cms.Menu')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('translatablepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailtrans.TranslatablePage')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
                ('theme_section_title', models.CharField(blank=True, help_text='Title to display above the theme section', max_length=255, null=True)),
                ('theme_section_intro', wagtail.core.fields.RichTextField(blank=True)),
                ('article_section_title', models.CharField(blank=True, help_text='Title to display above the article section', max_length=255, null=True)),
                ('article_section_intro', wagtail.core.fields.RichTextField(blank=True)),
                ('article_section', models.ForeignKey(blank=True, help_text='Featured articles for the homepage', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailtrans.TranslatablePage', verbose_name='Article section')),
                ('theme_section', models.ForeignKey(blank=True, help_text='Featured section for the homepage. Will display all themes.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailtrans.TranslatablePage', verbose_name='Theme section')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailtrans.translatablepage',),
        ),
        migrations.CreateModel(
            name='CustomComment',
            fields=[
                ('xtdcomment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_comments_xtd.XtdComment')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='customcomments', to='cms.ArticlePage')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'ordering': ('submit_date',),
                'permissions': [('can_moderate', 'Can moderate comments')],
                'abstract': False,
            },
            bases=('django_comments_xtd.xtdcomment',),
        ),
        migrations.CreateModel(
            name='CompanyLogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('logo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image')),
            ],
        ),
        migrations.AddField(
            model_name='articlepage',
            name='themes',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='articlepages', to='cms.Theme', verbose_name='Themes'),
        ),
        migrations.CreateModel(
            name='AdvancedFormSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_address', models.EmailField(max_length=254)),
                ('form', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='advanced_settings', to='wagtailstreamforms.Form')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]