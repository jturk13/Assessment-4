from flask import Flask, redirect, render_template, url_for
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)
db = SQLAlchemy(app)

from models import Playlist, Song, PlaylistSong

@app.route("/")
def root():
    """Homepage: redirect to /playlists."""
    return redirect("/playlists")

@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""
    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)

@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""
    playlist = Playlist.query.get_or_404(playlist_id)
    return render_template("playlist.html", playlist=playlist)

@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """
    form = PlaylistForm()
    if form.validate_on_submit():
        playlist = Playlist(name=form.name.data)
        db.session.add(playlist)
        db.session.commit()
        return redirect(url_for('show_all_playlists'))
    return render_template('add_playlist.html', form=form)

@app.route("/songs")
def show_all_songs():
    """Show list of songs."""
    songs = Song.query.all()
    return render_template("songs.html", songs=songs)

@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""
    song = Song.query.get_or_404(song_id)
    return render_template("song.html", song=song)

@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """
    form = SongForm()
    if form.validate_on_submit():
        song = Song(title=form.title.data, artist=form.artist.data)
        db.session.add(song)
        db.session.commit()
        return redirect(url_for('show_all_songs'))
    return render_template('add_song.html', form=form)

@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a song to a playlist and redirect to playlist."""
    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()
    form.song.choices = [(song.id, song.title) for song in Song.query.filter(~Song.playlists.any(id=playlist_id)).all()]
    if form.validate_on_submit():
        song_id = form.song.data
        playlist_song = PlaylistSong(playlist_id=playlist_id, song_id=song_id)
        db.session.add(playlist_song)
        db.session.commit()
        return redirect(url_for('show_playlist', playlist_id=playlist_id))
    return render_template("add_song_to_playlist.html", playlist=playlist, form=form)
