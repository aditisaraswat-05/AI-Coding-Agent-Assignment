const mongoose = require('mongoose');

const NoteSchema = mongoose.Schema({
    title: {
        type: String,
        required: true,
        trim: true
    },
    content: {
        type: String,
        required: true
    },
    tags: [{
        type: String,
        index: true
    }],
    category: {
        type: String,
        index: true,
        default: 'General'
    },
    folder: {
        type: String,
        index: true,
        default: 'Uncategorized'
    }
}, {
    timestamps: true
});

module.exports = mongoose.model('Note', NoteSchema);