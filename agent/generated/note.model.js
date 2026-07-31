const mongoose = require('mongoose');

const NoteSchema = mongoose.Schema({
    title: {
        type: String,
        required: true,
        trim: true,
        index: true
    },
    content: {
        type: String,
        required: true
    },
    category: {
        type: String,
        trim: true,
        index: true,
        default: 'General'
    },
    tags: [{
        type: String,
        trim: true,
        index: true
    }],
    folder: {
        type: String,
        index: true,
        default: 'Uncategorized'
    }
}, {
    timestamps: true
});

module.exports = mongoose.model('Note', NoteSchema);