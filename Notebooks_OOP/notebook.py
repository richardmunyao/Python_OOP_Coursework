import datetime

#global var to start the next available note id
last_id = 0

class Note:
    ''' This will represent a note in our notebook. Create a Memo with tags, and allow Search'''
    def __init__(self, memo, tags=''):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.datetime.now()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        '''match both memo and tags with the filter provided'''
        return filter in self.memo or filter in self.tags

class Notebook:
    '''Collection of Notes'''
    def __init__(self):
        '''Initialize notebook with empty list'''
        self.notes = []

    def new_note(self, memo, tags=''):
        '''Initialize new note, append to list of notes'''
        self.notes.append(Note(memo, tags=''))

    def _find_note(self, note_id):
        '''Locate note with given id. For internal use'''
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def modify_memo(self,note_id, memo):
        '''Find note, given id, and modify memo contents'''
        self._find_note(note_id).memo = memo
        
        
    def modify_tags(self, note_id, tags):
        '''Find note, given id, and modify memo tags'''
        self._find_note(note_id).tags = tags

    def search(self, filter):
        '''Find all notes that match filter string'''
        return [note for note in self.notes if note.match(filter)]
