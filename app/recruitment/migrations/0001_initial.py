# Generated by Django 5.0 on 2024-01-29 11:33

import autoslug.fields
import django.core.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('DRAFT', 'DRAFT'), ('INACTIVE', 'Inactive'), ('REMOVED', 'Removed')], db_index=True, default='ACTIVE', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.CharField(blank=True, max_length=200)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recruiter', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Recruiters',
            },
        ),
        migrations.CreateModel(
            name='OpenJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('DRAFT', 'DRAFT'), ('INACTIVE', 'Inactive'), ('REMOVED', 'Removed')], db_index=True, default='ACTIVE', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('internal_reference', models.CharField(blank=True, db_index=True, max_length=255, unique=True)),
                ('job_source', models.CharField(choices=[('BD_JOBS', 'Bd_Jobs'), ('INDEED', 'INDEED'), ('INTERNAL', 'Internal'), ('LINKEDIN', 'Likedin'), ('NEWS_PAPER', 'News_Paper'), ('RECRUITER', 'Recruiter'), ('OTHER', 'Other')], default='OTHER', max_length=255)),
                ('link', models.TextField(blank=True)),
                ('profession', models.CharField(blank=True, max_length=255)),
                ('raw_job', models.TextField(blank=True)),
                ('experience_year', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)])),
                ('required_skills', models.JSONField(blank=True, default=dict)),
                ('required_experiences', models.JSONField(blank=True, default=dict)),
                ('job_location', models.CharField(choices=[('ANYWHERE', 'Anywhere'), ('BAGERHAT', 'Bagerhat'), ('BAKHTEYARPUR', 'Bakhteyarpur'), ('BANDARBAN', 'Bandarban'), ('BARGUNA', 'Barguna'), ('BARISHAL', 'Barishal'), ('BHOLA', 'Bhola'), ('BOGRA', 'Bogra'), ('CHANDPUR', 'Chandpur'), ('CHAPAINAWABGANJ', 'Chapainawabganj'), ('CHHAGALNAIYA', 'Chhagalnaiya'), ('CHITTAGONG', 'Chittagong'), ('CHITTAGONG_PORT', 'Chittagong Port'), ('CHUADANGA', 'Chuadanga'), ('COX_S_BAZAR', "Cox's Bazar"), ('DHAKA', 'Dhaka'), ('COMILLA', 'Comilla'), ('FARIDPUR', 'Faridpur'), ('FENI', 'Feni'), ('GAZIPUR', 'Gazipur'), ('GOPALGANJ', 'Gopalganj'), ('HABIGANJ', 'Habiganj'), ('JESSORE', 'Jessore'), ('JHALOKATHI', 'Jhalokathi'), ('JHENIDAH', 'Jhenidah'), ('JOYPURHAT', 'Joypurhat'), ('KALIGANJ', 'Kaliganj'), ('KERANIGANJ', 'Keraniganj'), ('KHAGRACHARI', 'Khagrachari'), ('KISHOREGANJ', 'Kishoreganj'), ('KISHORGANJ', 'Kishorganj'), ('KHULNA', 'Khulna'), ('KUAKATA', 'Kuakata'), ('KURIGRAM', 'Kurigram'), ('KUSHTIA', 'Kushtia'), ('LAKSHMIPUR', 'Lakshmipur'), ('LALMONIRHAT', 'Lalmonirhat'), ('MAGURA', 'Magura'), ('MAULVI_BAZAR', 'Maulvi Bazar'), ('MADARIPUR', 'Madaripur'), ('MOHESHKHALI', 'Moheshkhali'), ('MYMENSINGH', 'Mymensingh'), ('NARAIL', 'Narail'), ('NARAYANGANJ', 'Narayanganj'), ('NARSINGDI', 'Narsingdi'), ('NARSHINGDI', 'Narshingdi'), ('NATORE', 'Natore'), ('NAOGAON', 'Naogaon'), ('NAWABGANJ', 'Nawabganj'), ('NILPHAMARI', 'Nilphamari'), ('PATUAKHALI', 'Patuakhali'), ('PABNA', 'Pabna'), ('PAIKGACHHA', 'Paikgachha'), ('PANCHAGARH', 'Panchagarh'), ('PARBATIPUR', 'Parbatipur'), ('PUTHIA', 'Puthia'), ('RAJBARI', 'Rajbari'), ('RAIPUR', 'Raipur'), ('RAJSHAHI', 'Rajshahi'), ('RANGPUR', 'Rangpur'), ('SARISHA', 'Sarisha'), ('SATKHIRA', 'Satkhira'), ('SABAIL', 'Sabail'), ('SANDWIP', 'Sandwip'), ('SHARANKHALI', 'Sharankhali'), ('SHYAMNAGAR', 'Shyamnagar'), ('SIRAJGANJ', 'Sirajganj'), ('SITAKUNDA', 'Sitakunda'), ('SUNAMGANJ', 'Sunamganj'), ('SYLHET', 'Sylhet'), ('TANGAIL', 'Tangail'), ('THAKURGAON', 'Thakurgaon'), ('TUNGIPARA', 'Tungipara'), ('ULLAHPARA', 'Ullahpara'), ('UNKNOWN', 'Unknown'), ('OTHER', 'Other')], default='OTHER', max_length=255)),
                ('job_type', models.CharField(choices=[('CONTRACTUAL', 'Contractual'), ('FULL_TIME', 'Full_Time'), ('PART_TIME', 'Part_Time'), ('PERMANENT', 'Permanent'), ('TEMPORARY', 'Temporary'), ('OTHER', 'OTHER')], default='OTHER', max_length=30)),
                ('job_category', models.CharField(choices=[('ANY', 'Any'), ('OFFICE', 'Office'), ('REMOTE', 'Remote'), ('HYBRID', 'Hybrid'), ('OTHER', 'Other')], default='OTHER', max_length=30)),
                ('job_status', models.CharField(choices=[('CLOSED', 'Closed'), ('DRAFT', 'DRAFT'), ('OPEN', 'Open'), ('PUBLISHED', 'Published'), ('REJECTED', 'Rejected')], default='DRAFT', max_length=30)),
                ('attachement', models.FileField(blank=True, null=True, upload_to='job-attachments')),
                ('recruiter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='open_jobs', to='recruitment.recruiter')),
            ],
            options={
                'verbose_name_plural': 'Open Jobs',
            },
        ),
    ]