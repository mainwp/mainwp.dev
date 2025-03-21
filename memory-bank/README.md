# Memory Bank

This directory contains Cline's memory bank files that are used to maintain context between sessions.

## Git Configuration

The files in this directory are configured to be:
- **Tracked locally**: The files are included in your local Git repository
- **Not pushed to GitHub**: Changes to these files won't be included in commits that you push to GitHub

This is achieved using Git's `skip-worktree` flag, which tells Git to pretend these files haven't been modified, even if you make changes to them.

## Working with Memory Bank Files

### Viewing the Status

To see which files have the `skip-worktree` flag set:

```bash
git ls-files -v | grep ^S
```

### Making Changes

You can edit the memory bank files normally. Git will ignore these changes when you commit and push.

### If You Need to Commit Changes

If you ever need to temporarily commit and push changes to these files, you can unset the `skip-worktree` flag:

```bash
# Unset the skip-worktree flag
git update-index --no-skip-worktree memory-bank/*

# Make your commits and push

# Set the skip-worktree flag again
git update-index --skip-worktree memory-bank/*
```

### If Someone Else Updates These Files

If someone else makes changes to these files on GitHub and you pull those changes, Git will warn you. You'll need to:

```bash
# Unset the skip-worktree flag
git update-index --no-skip-worktree memory-bank/*

# Pull the changes
git pull

# Set the skip-worktree flag again
git update-index --skip-worktree memory-bank/*
```

## Initial Setup

This configuration was set up with:

```bash
# Add the files to Git
git add memory-bank/

# Set the skip-worktree flag
git update-index --skip-worktree memory-bank/*
# Test change
