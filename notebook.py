"""  
Тут реалізований сам клас
"""
from collections import UserDict, OrderedDict

class NoteBook(UserDict):
    
    def add_note(self, title, text, tags=None):
        if tags is None:
            tags = []
        self.data[title] = {'text': text, 'tags': tags} 
    
    def edit_note(self, title, new_text=None, new_tags=None):
        if title in self.data:
            if new_text:
                self.data[title]['text'] = new_text
            if new_tags is not None:
                self.data[title]['tags'] = new_tags
    
    def delete_note(self, title):
        if title in self.data:
            del self.data[title]

    def search_notes(self, keyword):
        page = ''
        keyword = keyword.lower()  
        for title, note in self.data.items():
            if keyword in title.lower() or any(keyword in tag.lower() for tag in note['tags']):
                page += self.__str__(title)
        return page

    def sort_notes(self):
        sorted_data = sorted(self.data.items(), key=lambda x: (-len(x[1]['tags']), x[0]))
        self.data = OrderedDict(sorted_data)
        return self.__str__()
    
    def __iter__(self):
        for title, note in self.data.items():
            yield self.__str__(title)

    def __str__(self, title_to_print=None):
        if title_to_print:
            note = self.data.get(title_to_print)
            return "\n<<<{}>>>\n{}\ntags: {}\n".format(title_to_print, note['text'], note['tags'])
        else:
            result = ""
            for title, note in self.data.items():
                result += "\n<<<{}>>>\n{}\ntags: {}\n".format(title, note['text'], note['tags'])
            return result