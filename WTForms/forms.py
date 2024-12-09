from wtforms import Form
from wtforms.fields import(
    StringField, IntegerField, PasswordField, DateField, RadioField, 
    SelectField, BooleanField, TextAreaField,EmailField, SubmitField
)
#使用するバリデーターをインポート
from wtforms.validators import(
    #入力必須
    DataRequired, 
    #フィールド同士の比較
    EqualTo,
    #文字列の長さ指定
    Length,
    #数値の範囲指定
    NumberRange,
    #メールアドレスの形式か
    Email
)

class UserInfoForm(Form):
    #氏名：文字列入力
    name = StringField(
        '氏名', 
        render_kw={'placeholder':'バンタン二郎'},
        validators=[DataRequired('氏名の入力は必須です')] 
        )

    # 年齢：数値入力
    age = IntegerField(
        '年齢', 
        default=20,
        validators=[NumberRange(20,120,'入力範囲は20から120です')]
        
        )

    #パスワード：パスワード入力
    password = PasswordField(
        'パスワード',
        validators=[Length(8,16,'パスワードの長さは8文字以上16文字以内です'),
                    EqualTo('confirm_password','パスワードが一致しません')]
        )

    #パスワード確認用
    confirm_password = PasswordField(
        'パスワード確認'
        )

    #Email:メールアドレス
    email = EmailField(
        'メールアドレス', 
        render_kw={'placeholder':'bantan@bantan.com'},
        validators=[Email('メールアドレスのフォーマットではありません')]
        )

    #生年月日：カレンダー入力
    birthday = DateField(
        '生年月日', 
        format='%Y-%m-%d',
        validators=[DataRequired('生年月日の入力は必須です。')]
        )

    #性別：ラジオボタン
    gender = RadioField('性別', choices=[('man','男性'),('woman','女性'),('others','他の人')], default='woman')

    # 出身地域：セレクトボックス
    area = SelectField('出身地域',choices=[('east','東日本'),('west','西日本')])

    #備考欄：複数行テキスト
    comment = TextAreaField(
        '備考欄',
        # render_kw={'placeholder':"文字数は400文字以内でお願いします。"}
        # validators=[]
        )

    # 真偽地
    terms = BooleanField(
        '利用規約に同意しますか？',
        validators=[DataRequired('利用規約への同意は必須です')]
        )

    #ボタン
    submit = SubmitField('送信')