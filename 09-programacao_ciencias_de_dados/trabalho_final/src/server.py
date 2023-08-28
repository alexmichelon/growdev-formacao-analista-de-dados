from flask import Flask
import controllers.rotes as rotes

app = Flask(__name__)

app.add_url_rule('/', view_func=rotes.index)
app.add_url_rule('/database/search', view_func=rotes.search_data, methods=['GET','POST'])
app.add_url_rule('/database/group_by', view_func=rotes.group_by_data, methods=['GET','POST'])
app.add_url_rule('/database/search_group_by', view_func=rotes.search_group_by_data, methods=['GET','POST'])
app.add_url_rule('/database/describe_info', view_func=rotes.describe_info, methods=['GET','POST'])

if __name__ == "__main__":
    app.run(debug=True, port=80)