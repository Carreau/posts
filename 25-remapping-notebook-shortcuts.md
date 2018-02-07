<!-- 
.. title: Remapping notebook shortcuts
.. slug: 25-remaping-notebook-shortcuts.md
.. date: 2016-11-30 11:00:00 UTC
.. type: text
-->


As Jupyter notebook run in a browser for technical and practical
reasons we only have a limited number of shortcuts available and
choices need to be made. Often this choices may conflict with browser
shortcut, and you might need to remap it. 

Today I was inform by Stefan van Der Walt that `Cmd-Shift-P` conflict
for Firefox. It is mapped both to open the _Command palette_ for the
notebook and  open a new _Private Browsing_ window. 

Using _Private Browsing_ windows is extremely useful. When developing
a website you might want to look at it without being logged in, and
with an empty cache. So let see how we can remap the Jupyter notebook
shortcut. 

## TL; DR;

Use the following in your `~/.jupyter/custom/custom.js` :


    require(['base/js/namespace'], function(Jupyter){
      // we might want to but that in a callback on wait for 
      // en even telling us the ntebook is ready.
      console.log('== remaping command palette shortcut ==')
      // note that meta is the command key on mac.
      var source_sht = 'meta-shift-p'
      var target_sht = 'meta-/'
      var cmd_shortcuts = Jupyter.keyboard_manager.command_shortcuts;
      var action_name = cmd_shortcuts.get_shortcut(source_sht)
      cmd_shortcuts.add_shortcut(target_sht, action_name)
      cmd_shortcuts.remove_shortcut(source_sht)
      console.log('== ', action_name, 'remaped from', source_sht, 'to', target_sht )
    })

## details

We need to use `require` and register a callback once the notebook is
loaded:

```
require(['base/js/namespace'], function(Jupyter){
  ...
})
```

Here we grab the main namespace and name it Jupyter.

Then get the object that hold the various shortcuts: `var
cmd_shortcuts = Jupyter.keyboard_manager.command_shortcuts`.

Shortcuts are define by sequence on keys with modifiers. Modifiers are
dash-separated (need to be pressed at the same time). Sequence are
comma separated. Example quiting in vim would be `esc,;,w,q`, in emacs
`ctrl-x,ctrl-c`. 

Here we want to unbind `meta-shift-p` (`p` is lowercase despite shift
being pressed) and bind `meta-/` (The shortcut Stefan wants). Note
that `meta-` is the command key on mac.

We need to get the current command bound to this shortcut
(`cmd_shortcuts.get_shortcut(source_sht)`). You could hardcode the
name of the command but it may change a bit depending on notebook
version (this is not yet public API). Here it is `jupyter-notebook:show-command-palette`. 

You now bind it to your new shortcut:

```
cmd_shortcuts.add_shortcut('meta-/', action_name)
```

And finally unbind the original one

```
cmd_shortcuts.remove_shortcut('meta-shift-p')
```

## UI reflect your changes !

If you open the command palette, you should see that the `Show command
palette` command now display `Command-/` as its shortcut !

## Future

We are working on an interface to edit shortcuts directly from within
the UI and not to have to write a single line of code !

Questions, feedback and fixes [welcomed](https://github.com/carreau/posts)
