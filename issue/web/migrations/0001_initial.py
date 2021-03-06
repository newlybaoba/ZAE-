# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-03-25 09:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.CharField(max_length=200, verbose_name='命令')),
                ('result', models.CharField(max_length=2000, verbose_name='结果')),
                ('hosts_list', models.CharField(max_length=20000, verbose_name='执行机器')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Cron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='计划名称')),
                ('note', models.CharField(blank=True, max_length=256, null=True, verbose_name='计划描述')),
                ('user', models.CharField(blank=True, default='root', max_length=256, null=True, verbose_name='执行用户')),
                ('job', models.CharField(max_length=64, verbose_name='计划')),
                ('time', models.CharField(max_length=64, verbose_name='计划任务执行的时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='主机名')),
                ('hostip', models.GenericIPAddressField(verbose_name='主机ip地址')),
                ('settings', models.CharField(choices=[('0', '开发'), ('1', '测试'), ('2', '准生产'), ('3', '生产')], default='0', max_length=20, verbose_name='环境')),
                ('type', models.CharField(choices=[('0', 'nginx'), ('1', 'other')], default='1', max_length=20, verbose_name='类型')),
                ('ssh_port', models.CharField(default=22, max_length=10, verbose_name='ssh端口')),
            ],
        ),
        migrations.CreateModel(
            name='Host_Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('0', '等待更新'), ('1', '更新中'), ('2', '等待测试'), ('3', '测试通过'), ('4', '更新完成'), ('5', '更新失败'), ('6', '回滚成功')], default='0', max_length=20, verbose_name='更新状态')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Host', verbose_name='发布机器')),
            ],
            options={
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('0', '文件'), ('1', 'git')], default='0', max_length=20, verbose_name='更新类型')),
                ('status', models.CharField(choices=[('0', '等待更新'), ('1', '更新中'), ('2', '等待测试'), ('3', '测试通过'), ('4', '更新完成'), ('5', '更新失败'), ('6', '回滚成功')], default='0', max_length=20, verbose_name='更新状态')),
                ('backup', models.CharField(choices=[('0', '是'), ('1', '否')], default='0', max_length=20, verbose_name='备份状态')),
                ('path', models.CharField(blank=True, max_length=2048, null=True, verbose_name='备份文件路径')),
                ('src_path', models.CharField(blank=True, max_length=2048, null=True, verbose_name='上传文件路径')),
            ],
            options={
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='项目名')),
                ('path', models.CharField(max_length=200, verbose_name='项目目录')),
                ('git_path', models.CharField(max_length=200, verbose_name='git地址')),
                ('nginxconf', models.CharField(blank=True, max_length=200, null=True, verbose_name='nginx配置文件')),
                ('nginxupstream', models.CharField(blank=True, max_length=200, null=True, verbose_name='nginx upstream名称')),
                ('language', models.CharField(choices=[('0', 'python'), ('1', 'java'), ('2', 'go'), ('3', 'php'), ('4', 'html')], default='0', max_length=20, verbose_name='语言')),
                ('domain', models.CharField(blank=True, max_length=100, null=True, verbose_name='域名')),
                ('note', models.CharField(blank=True, max_length=218, null=True, verbose_name='备注信息')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('host', models.ManyToManyField(related_name='upstarm机器', to='web.Host', verbose_name='后端主机')),
                ('nginxhost', models.ManyToManyField(related_name='nginx', to='web.Host', verbose_name='nginx机器')),
            ],
            options={
                'ordering': ('-create_time',),
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='用户名称')),
                ('email', models.CharField(max_length=200, verbose_name='邮箱地址')),
                ('password', models.CharField(max_length=200, verbose_name='密码')),
                ('role', models.CharField(choices=[('0', '开发'), ('1', '测试'), ('2', '运维')], default='0', max_length=10, verbose_name='角色')),
                ('isAdmin', models.CharField(choices=[('0', 'Admin'), ('1', '普通')], default='1', max_length=10, verbose_name='管理员')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('phone', models.BigIntegerField(blank=True, null=True, verbose_name='手机号')),
            ],
            options={
                'ordering': ['-create_time'],
            },
        ),
        migrations.AddField(
            model_name='team',
            name='test_user',
            field=models.ManyToManyField(related_name='测试人员', to='web.UserProfile', verbose_name='测试人员'),
        ),
        migrations.AddField(
            model_name='team',
            name='user_id',
            field=models.ManyToManyField(related_name='研发人员', to='web.UserProfile', verbose_name='研发人员'),
        ),
        migrations.AddField(
            model_name='issue',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Team', verbose_name='发布项目'),
        ),
        migrations.AddField(
            model_name='issue',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.UserProfile', verbose_name='发布人'),
        ),
        migrations.AddField(
            model_name='host_issue',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Issue', verbose_name='更新'),
        ),
        migrations.AddField(
            model_name='host_issue',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Team', verbose_name='发布项目'),
        ),
        migrations.AddField(
            model_name='cron',
            name='create_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.UserProfile', verbose_name='创建者'),
        ),
        migrations.AddField(
            model_name='cron',
            name='host',
            field=models.ManyToManyField(max_length=500, to='web.Host', verbose_name='任务机器'),
        ),
        migrations.AddField(
            model_name='command',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.UserProfile', verbose_name='用户'),
        ),
    ]
