# Notes:

After playing around with Canny Edge detection I noticed that isolating strictly the board and hexagonal edges between the tiles was tiresome an unfruitful. See below

![Edges](smalledges.png)

However, by accident I noticed that doing so made the roll number tiles isolate in nearly full detail in black and white.

![NumTile](tile.png)

# Solution?

I now believe that there is still hope on the horizon. I think the next step is trying to do **Markerless Tracking** of the tiles on the board.
This works by taking images and comparing them to other images, in our case a video feed, to try and located them in the video feed. See below for example

![MarkTrack](markerlesstracking.png)

I think that with this approach we can not only identify the tiles on the board and the marker tiles, but we can also eliminate the need for any OCR on the marker tiles because we will be associating them with known data instead of having to figure out what data is being held in them.