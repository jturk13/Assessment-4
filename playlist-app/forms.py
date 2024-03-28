from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Create Playlist')

class SongForm(FlaskForm):
    """Form for adding songs."""
    title = StringField('Title', validators=[DataRequired()])
    artist = StringField('Artist', validators=[DataRequired()])
    submit = SubmitField('Create Song')

class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""
    song = SelectField('Song To Add', coerce=int)
    submit = SubmitField('Add Song')
