from app import create_app, db

app = create_app()

# 初始化数据库（只在首次运行时需要）
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
