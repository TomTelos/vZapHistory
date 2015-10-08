try:
    from Components.LanguageGOS import gosgettext as _
except:
    from Components.Language import language
    from Tools.Directories import SCOPE_PLUGINS
    import gettext
    PluginLanguageDomain = "vZapHistory"
    PluginLanguagePath = "Extensions/vZapHistory/locale"
    def localeInit():
        lang = language.getLanguage()[:2]
        os.environ["LANGUAGE"] = lang
        gettext.bindtextdomain(PluginLanguageDomain, resolveFilename(SCOPE_PLUGINS, PluginLanguagePath))
    def _(txt):
        t = gettext.dgettext(PluginLanguageDomain, txt)
        if t == txt:
            t = gettext.gettext(txt)
        return t
    localeInit()
    language.addCallback(localeInit)
    
